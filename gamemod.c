#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// 版本定義
#define VERSION "1.0.0"
#define VERSION_DATE "2026-01-22"

typedef struct {
    int betCount;
    int initBalance;
    int stopWin;
    int stopLoss;
    int winRate;
    int minBet;
    int winRateDecrement;
} Config;

typedef struct {
    int balance;
    int totalWin;
    int totalLoss;
    int totalBet;
    int gamesPlayed;
    int profit;
} GameStats;

// 顯示版本信息
void show_version() {
    printf("馬丁格爾策略模擬器 版本 %s\n", VERSION);
    printf("編譯日期: %s\n", VERSION_DATE);
    printf("作者: 遊戲模組\n");
}

// 解析命令行參數
int parse_args(int argc, char *argv[], Config *config) {
    // 設置默認值
    config->betCount = 1000;
    config->initBalance = 20000;
    config->stopWin = 50000;
    config->stopLoss = 30000;
    config->winRate = 80;
    config->minBet = 100;
    config->winRateDecrement = 5;
    
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-bets") == 0 && i + 1 < argc) {
            config->betCount = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-balance") == 0 && i + 1 < argc) {
            config->initBalance = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-stopwin") == 0 && i + 1 < argc) {
            config->stopWin = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-stoploss") == 0 && i + 1 < argc) {
            config->stopLoss = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-winrate") == 0 && i + 1 < argc) {
            config->winRate = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-minbet") == 0 && i + 1 < argc) {
            config->minBet = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-decrement") == 0 && i + 1 < argc) {
            config->winRateDecrement = atoi(argv[++i]);
        } else if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--version") == 0) {
            show_version();
            return 0;
        } else if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            printf("使用方式: %s [選項]\n", argv[0]);
            printf("選項:\n");
            printf("  -bets <次數>      下注次數 (預設: 1000)\n");
            printf("  -balance <金額>   初始餘額 (預設: 20000)\n");
            printf("  -stopwin <金額>   止盈金額 (預設: 50000)\n");
            printf("  -stoploss <金額>  止損金額 (預設: 30000)\n");
            printf("  -winrate <百分比> 勝率 (預設: 80)\n");
            printf("  -minbet <金額>    最小下注額 (預設: 100)\n");
            printf("  -decrement <值>   每10局勝率遞減值 (預設: 5)\n");
            printf("  -v, --version     顯示版本資訊\n");
            printf("  -h, --help        顯示幫助訊息\n");
            return 0;
        }
    }
    return 1;
}

// 初始化遊戲統計
void init_stats(GameStats *stats, Config *config) {
    stats->balance = config->initBalance;
    stats->totalWin = 0;
    stats->totalLoss = 0;
    stats->totalBet = 0;
    stats->gamesPlayed = 0;
    stats->profit = 0;
}

// 根據索引獲取下注金額
int get_bet_amount(int index, int *maxNumber, int maxNumberSize) {
    if (index < 0 || index >= maxNumberSize) {
        return maxNumber[maxNumberSize - 1];
    }
    return maxNumber[index];
}

// 模擬遊戲
void simulate_game(Config *config, GameStats *stats) {
    printf("初始餘額: %d\n", stats->balance);
    
    // 初始化最大下注數組
    int maxNumberSize = 9;
    int *maxNumber = (int *)malloc(sizeof(int) * maxNumberSize);
    if (!maxNumber) {
        printf("記憶體分配失敗！\n");
        return;
    }
    
    // 填充數組：100, 200, 400, ..., 25600
    maxNumber[0] = config->minBet;
    for (int i = 1; i < maxNumberSize; i++) {
        maxNumber[i] = maxNumber[i - 1] * 2;
    }
    
    int currBet = maxNumber[0];
    int currentWinRate = config->winRate;
    int lossStreak = 0;
    
    srand((unsigned int)time(NULL)); // 設置隨機種子
    
    for (int i = 0; i < config->betCount; i++) {
        // 檢查停止條件
        if (stats->balance < currBet) {
            printf("已經破產，無法繼續 (餘額: %d, 需要: %d)\n", stats->balance, currBet);
            break;
        }
        
        if (stats->balance >= config->initBalance + config->stopWin) {
            printf("停止獲利 (餘額: %d, 目標: %d)\n", 
                   stats->balance, config->initBalance + config->stopWin);
            break;
        }
        
        if (stats->balance <= config->initBalance - config->stopLoss) {
            printf("停止虧損 (餘額: %d, 底線: %d)\n", 
                   stats->balance, config->initBalance - config->stopLoss);
            break;
        }
        
        if (stats->balance < config->minBet) {
            printf("餘額已低於最小下注額（%d），遊戲結束\n", config->minBet);
            break;
        }
        
        // 執行下注
        int thisBet = currBet;
        stats->balance -= thisBet;
        stats->totalBet += thisBet;
        stats->gamesPlayed++;
        
        // 模擬勝負
        int randomValue = rand() % 100;
        int result = (randomValue < currentWinRate) ? 1 : 0;
        
        if (result == 1) { // 贏
            stats->balance += thisBet * 2;
            currBet = maxNumber[0]; // 重置下注金額
            stats->totalWin += thisBet;
            lossStreak = 0;
            printf("第%d局: 贏 %d, 餘額: %d\n", i + 1, thisBet, stats->balance);
        } else { // 輸
            // 使用馬丁格爾策略增加下注
            lossStreak++;
            if (lossStreak < maxNumberSize) {
                currBet = maxNumber[lossStreak];
            } else {
                currBet = maxNumber[maxNumberSize - 1];
            }
            stats->totalLoss += thisBet;
            printf("第%d局: 輸 -%d, 餘額: %d\n", i + 1, thisBet, stats->balance);
        }
        
        // 每10局調整勝率
        if ((i + 1) % 10 == 0) {
            currentWinRate -= rand() % config->winRateDecrement;
            if (currentWinRate < 0) currentWinRate = 0;
            printf("--- 已完成 %d 局，餘額: %d，勝率調整為: %d%% ---\n", 
                   i + 1, stats->balance, currentWinRate);
        }
    }
    
    // 計算最終利潤
    stats->profit = stats->balance - config->initBalance;
    
    // 輸出統計結果
    printf("\n========== 遊戲統計 ==========\n");
    printf("總局數: %d\n", stats->gamesPlayed);
    printf("初始餘額: %d\n", config->initBalance);
    printf("最終餘額: %d\n", stats->balance);
    printf("利潤: %d\n", stats->profit);
    
    if (stats->totalBet > 0) {
        double winPercent = (stats->totalWin * 100.0) / stats->totalBet;
        double lossPercent = (stats->totalLoss * 100.0) / stats->totalBet;
        printf("贏錢比例: %.2f%%\n", winPercent);
        printf("輸錢比例: %.2f%%\n", lossPercent);
        printf("總下注金額: %d\n", stats->totalBet);
        printf("淨勝率: %.2f%%\n", ((double)stats->totalWin - stats->totalLoss) / stats->totalBet * 100);
    }
    
    printf("=============================\n");
    
    // 釋放記憶體
    free(maxNumber);
}

int main(int argc, char *argv[]) {
    Config config;
    GameStats stats;
    
    // 解析命令行參數
    if (!parse_args(argc, argv, &config)) {
        return 0;
    }
    
    // 驗證參數
    if (config.betCount <= 0 || config.initBalance <= 0 || 
        config.winRate < 0 || config.winRate > 100) {
        printf("錯誤：無效的參數值！\n");
        return 1;
    }
    
    // 初始化並運行遊戲
    init_stats(&stats, &config);
    simulate_game(&config, &stats);
    
    return 0;
}