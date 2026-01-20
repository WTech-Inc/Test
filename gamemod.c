#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>

// 結構體定義
typedef struct {
    int level;
    char* name;
    int min_flow;
} RewardLevel;

typedef struct {
    int flowWater;
    int commission;
    int points;
    double commissionRate;
} RewardInfo;

typedef struct {
    int balance;
    int totalBet;
    int totalWin;
    int totalLoss;
    int profit;
} GameStats;

// 函數宣告
RewardInfo* calculate_rewards(int flowWater);
void display_rewards(RewardInfo* info);
void free_reward_info(RewardInfo* info);
void simulate_game(int betCount, int initBalance, GameStats* stats);

// 全域配置緩衝區（減少重複分配）
static char resultBuffer[3][10] = {"閒", "莊", "和"};
static char playerBuffer[3][10] = {"閒", "莊", "和"};

int main() {
    // 設定隨機種子
    srand((unsigned int)time(NULL));
    
    // 初始化遊戲統計
    GameStats* stats = (GameStats*)calloc(1, sizeof(GameStats));
    if (!stats) {
        fprintf(stderr, "記憶體分配失敗\n");
        return 1;
    }
    
    // 模擬遊戲
    simulate_game(5000, 400000, stats);
    
    // 顯示結果
    printf("\n利潤: %d\n", stats->profit);
    printf("戰後餘額: %d\n", stats->balance);
    
    if (stats->totalBet > 0) {
        double turnoverRatio = (double)stats->totalBet / 400000.0;
        printf("基本流水: %d\n", stats->totalBet);
        printf("積分倍數: %.2f倍\n", turnoverRatio);
        
        // 計算並顯示獎勵
        RewardInfo* rewards = calculate_rewards(stats->totalBet);
        if (rewards) {
            display_rewards(rewards);
            free_reward_info(rewards);
        }
    }
    
    // 釋放記憶體
    free(stats);
    
    return 0;
}

// 優化版本：預先計算並儲存下注階梯
void simulate_game(int betCount, int initBalance, GameStats* stats) {
    // 預先計算下注階梯大小
    const int maxNumber[] = {10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 
                             210, 230, 250, 270, 290, 310, 330, 350, 370, 390};
    const int maxNumberSize = sizeof(maxNumber) / sizeof(maxNumber[0]);
    
    // 遊戲參數
    int balance = initBalance;
    int currBet = maxNumber[0];
    const int stopWin = 200000;
    const int stopLoss = 50000;
    int winRate = 12;
    int j = 0;
    int winAmount = 0;
    
    // 開牌週期（使用靜態變數減少隨機數生成）
    static int openPlayerNumber = 0;
    static int openBankerNumber = 0;
    static int openTieNumber = 0;
    static bool initialized = false;
    
    if (!initialized) {
        openPlayerNumber = 3 + (rand() % 11);
        openBankerNumber = 5 + (rand() % 8);
        openTieNumber = 7 + (rand() % 3);
        initialized = true;
    }
    
    printf("初始餘額: %d\n", balance);
    printf("0-閒, 1-莊, 2-和\n");
    
    for (int i = 0; i < betCount; i++) {
        // 檢查停止條件
        if (balance < currBet) {
            printf("已經破產，無法繼續\n");
            break;
        }
        
        int winThreshold = initBalance + stopWin;
        int lossThreshold = initBalance - stopLoss;
        
        if (balance >= winThreshold) {
            printf("停止獲利\n");
            break;
        }
        
        if (balance <= lossThreshold) {
            printf("停止虧損\n");
            break;
        }
        
        // 下注
        int thisBet = currBet;
        balance -= thisBet;
        stats->totalBet += thisBet;
        
        // 玩家選擇和遊戲結果
        int playerSelect = rand() % 3;
        int gameResult = rand() % 3;
        
        // 動態調整開牌週期
        if (winRate < 40) {
            openPlayerNumber = (openPlayerNumber > 2) ? openPlayerNumber - 1 : 2;
        } else if (winRate > 60) {
            openPlayerNumber = (openPlayerNumber < 15) ? openPlayerNumber + 1 : 15;
        }
        
        // 週期性開牌
        if ((i + 1) % openPlayerNumber == 0) { 
            gameResult = 0; 
        } else if ((i + 1) % openBankerNumber == 0) { 
            gameResult = 1; 
        } else if ((i + 1) % openTieNumber == 0) { 
            gameResult = 2; 
        }
        
        // 計算結果
        int result = (playerSelect == gameResult) ? 1 : 0;
        
        // 使用緩衝區減少字串分配
        const char* gameResultText = resultBuffer[gameResult];
        const char* playerText = playerBuffer[playerSelect];
        
        if (result == 1) {
            // 計算贏錢金額
            if (gameResult == 2) { // 和
                winAmount = thisBet * 8;
                balance += thisBet + winAmount;
            } else if (gameResult == 1) { // 莊
                winAmount = (int)(thisBet * 0.95);
                balance += thisBet + winAmount;
            } else { // 閒
                winAmount = thisBet;
                balance += thisBet + winAmount;
            }
            
            // 調整下注階梯
            if (j < maxNumberSize - 1) {
                j++;
                currBet = maxNumber[j];
            }
            
            stats->totalWin += thisBet + winAmount;
            printf("開 %s , 贏 %d , 買 %s, 買入: %d, 餘額: %d\n", 
                   gameResultText, winAmount, playerText, thisBet, balance);
        } else {
            // 輸錢
            if (j > 0) {
                j--;
            }
            currBet = maxNumber[j];
            stats->totalLoss += thisBet;
            printf("開 %s, 輸 -%d , 買 %s, 買入: %d, 餘額: %d\n", 
                   gameResultText, thisBet, playerText, thisBet, balance);
        }
        
        // 檢查最小餘額
        if (balance < 100) {
            printf("餘額已低於最小下注額（100），遊戲結束\n");
            break;
        }
        
        // 動態調整勝率（使用查表法優化）
        static const int rateAdjustments[][2] = {
            {10, 2}, {20, 8}, {30, -9}, {40, -3}, {50, 5}, {80, -4}
        };
        
        for (int k = 0; k < 6; k++) {
            if ((i + 1) % rateAdjustments[k][0] == 0) {
                winRate += rateAdjustments[k][1];
                break;
            }
        }
        
        // 每10局顯示進度
        if ((i + 1) % 10 == 0) {
            printf("---每10局, 已完成%d局，餘額: %d---\n", i + 1, balance);
        }
    }
    
    // 更新統計資料
    stats->balance = balance;
    stats->profit = balance - initBalance;
}

// 計算獎勵資訊
RewardInfo* calculate_rewards(int flowWater) {
    RewardInfo* info = (RewardInfo*)malloc(sizeof(RewardInfo));
    if (!info) return NULL;
    
    info->flowWater = flowWater;
    info->commissionRate = 0.01;
    info->commission = (int)(flowWater * info->commissionRate);
    info->points = flowWater / 1000;
    
    return info;
}

// 顯示獎勵資訊
void display_rewards(RewardInfo* info) {
    if (!info) return;
    
    printf("\n=== 葡京娛樂城貴賓福利 ===\n");
    printf("  尊貴會員，您本次累積流水：%d 港元\n", info->flowWater);
    
    printf("\n【會員等級】\n");
    
    if (info->flowWater >= 1000000) {
        printf("  鑽石級貴賓（流水百萬以上）\n");
    } else if (info->flowWater >= 500000) {
        printf("  白金級貴賓（流水50萬以上）\n");
    } else if (info->flowWater >= 200000) {
        printf("  黃金級貴賓（流水20萬以上）\n");
    } else if (info->flowWater >= 50000) {
        printf("  白銀級貴賓（流水5萬以上）\n");
    } else if (info->flowWater >= 10000) {
        printf("  紅寶石會員（流水1萬以上）\n");
    } else if (info->flowWater >= 5000) {
        printf("  藍寶石會員（流水5千以上）\n");
    } else if (info->flowWater >= 1000) {
        printf("  翡翠會員（流水1千以上）\n");
    } else {
        printf("  普通會員\n");
        return;
    }
    
    printf("\n【碼糧回贈】\n");
    printf("  獲得現金碼糧：%d 港元（%.1f%%）\n", 
           info->commission, info->commissionRate * 100);
    
    printf("\n【娛樂積分】\n");
    printf("  累計積分：%d 分（可兌換各種獎品）\n", info->points);
    
    // 簡化顯示，只顯示主要福利
    printf("\n【主要福利】\n");
    if (info->flowWater >= 1000) {
        printf("  港澳高速船票 1張\n");
    }
    if (info->flowWater >= 5000) {
        printf("  葡京酒店標準房 1晚\n");
        printf("  葡京日麗餐廳 100港元餐券\n");
    }
    if (info->flowWater >= 20000) {
        printf("  四五六上海酒菜館 500港元餐券\n");
    }
    if (info->flowWater >= 50000) {
        printf("  新葡京酒店套房 3晚\n");
        printf("  免傭百家樂專桌\n");
    }
    if (info->flowWater >= 200000) {
        printf("  總統套房體驗 1晚\n");
        printf("  私人賭廳專屬包廂使用權\n");
    }
    if (info->flowWater >= 1000000) {
        printf("  全年免費住宿 + 私人飛機接送\n");
    }
    
    // 聯絡方式
    printf("\n【貴賓專線】\n");
    printf("  如需預訂福利，請聯絡您的貴賓經理：\n");
    printf("  電話：+853 2837 6666\n");
    
    // 免責聲明
    printf("\n【重要提示】\n");
    printf("  • 所有福利需提前3天預訂\n");
    printf("  • 福利不可兌換現金\n");
    printf("  • 賭博有風險，請理性投注\n");
    printf("  • 未滿21歲人士禁止進入賭場\n");
}

// 釋放獎勵資訊
void free_reward_info(RewardInfo* info) {
    if (info) free(info);
}