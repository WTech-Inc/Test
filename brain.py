import numpy as np
from math import floor

class NeuralNode:
    def __init__(self, weight=0, bias=0):
        """
        初始化神經節點 (Neural Node) 物件。

        參數:
            weight (float, 可選): 神經節點的權重。如果未提供，則隨機初始化為 0 到 0.01 之間的小數值。
            bias (float, 可選): 神經節點的偏置。如果未提供，則隨機初始化為 0 到 0.001 之間的小數值。
        """
        self.weight = weight if weight is not None else np.random.rand() * 0.01  # 初始化權重，如果 weight 為 None，則隨機取值
        self.bias = bias if bias is not None else np.random.rand() * 0.001   # 初始化偏置，如果 bias 為 None，則隨機取值

    def sigmoid(self, z):
        """
        Sigmoid 激活函數。

        Sigmoid 函數將輸入值壓縮到 0 和 1 之間。
        公式: 1 / (1 + exp(-z))

        參數:
            z (float): 輸入值 (加權求和 + 偏置)。

        返回:
            float: 經過 Sigmoid 函數激活後的輸出值，範圍在 0 到 1 之間。
        """
        # Sigmoid 函數的數學公式
        return 1 / (1 + np.exp(-z))

    def compute(self, inputs):
        """
        計算神經節點的輸出。

        1. 計算輸入的加權求和 (weighted sum) 並加上偏置 (bias)。
        2. 使用 Sigmoid 激活函數對加權求和結果進行激活。

        參數:
            inputs (list of float): 輸入值列表。

        返回:
            float: 神經節點的輸出值 (經過 Sigmoid 激活)。
        """
        # 計算加權求和：將每個輸入值乘以相同的權重，然後加總
        weighted_sum = sum(i * self.weight for i in inputs) + self.bias
        # 使用 Sigmoid 激活函數，將加權求和結果轉換為 0 到 1 之間的輸出
        return self.sigmoid(weighted_sum)

class Brain:
    def __init__(self):
        """
        初始化 Brain (大腦/神經網路) 物件。

        Brain 物件包含一個由 NeuralNode 組成的員工列表 (staff) 和一個輸出層 (outLayer)。
        """
        # 建立一個包含 3 個 NeuralNode 物件的列表，作為神經網路的隱藏層 (或員工層)
        self.staff = [NeuralNode() for _ in range(3)]  # 員工list
        # 建立一個 NeuralNode 物件作為神經網路的輸出層
        self.outLayer = NeuralNode()

    def normalize(self, inputs):
        """
        正規化輸入數據。

        將輸入值縮放到 0 到 1 之間，使用最大值正規化方法。
        正規化有助於提升神經網路訓練的效率和穩定性。

        參數:
            inputs (list of float): 原始輸入值列表。

        返回:
            list of float: 正規化後的輸入值列表。
        """
        # 根據數據集的最大值設置，用於正規化輸入數據
        max_values = [30000, 40000, 50000]  # 根據數據集的最大值設置
        normalized = []
        # 遍歷輸入值和對應的最大值
        for x, max_val in zip(inputs, max_values):
            # 防止除以零的錯誤，如果最大值為 0，則正規化值為 0
            if max_val == 0:
                normalized.append(0)  # 防止除以零
            else:
                # 最大值正規化: 將輸入值除以最大值，縮放到 0 到 1 之間
                normalized.append(x / max_val)
        return normalized

    def input(self, inputs):
        """
        接收輸入信號並進行正規化。

        參數:
            inputs (list of float): 原始輸入值列表。
        """
        # 正規化輸入值並儲存到 self.inputs 屬性
        self.inputs = self.normalize(inputs)

    def process(self):
        """
        處理輸入信號，執行神經網路的前向傳播。

        1. 將正規化後的輸入值傳遞給每個員工 (staff) 神經節點，計算每個節點的輸出。
        2. 將員工層的輸出作為輸入，傳遞給輸出層神經節點 (outLayer)，計算最終輸出。
        """
        # 對每個員工神經元計算輸出，使用正規化後的輸入
        self.firstOutput = [ node.compute(self.inputs) for node in self.staff]
        # 使用員工層的輸出作為輸入，計算輸出層神經元的輸出，得到最終的神經網路輸出
        self.outputs = self.outLayer.compute(self.firstOutput)

    def output(self):
        """
        返回神經網路的最終輸出。

        返回:
            float: 神經網路的輸出值。
        """
        return self.outputs

    def train(self, dataset, epochs=80):
        """
        訓練神經網路模型。

        使用提供的數據集 (dataset) 訓練神經網路，調整神經節點的權重和偏置，以降低輸出誤差。
        訓練過程使用簡化的梯度下降方法。

        參數:
            dataset (list of tuple): 訓練數據集，每個元素為一個元組 (input, target)。
                                      input (list of float): 輸入特徵列表。
                                      target (list of float): 目標輸出值列表。
            epochs (int, 可選): 訓練週期數，默認為 80。
        """
        # 迭代訓練週期
        for _ in range(epochs):
            # 迭代數據集中的每個樣本
            for input, target in dataset:
                # 輸入數據並進行前向傳播
                self.input(input)
                self.process()
                # 計算輸出誤差
                error = target[0] - self.outputs

                # 更新員工層 (staff) 神經元的權重和偏置
                for i ,  node in enumerate(self.staff):
                    # 使用簡化的梯度下降方法更新權重： 權重更新量 = 學習率 * 誤差 * 輸入值 (這裡只使用第一個輸入值)
                    node.weight += 0.0001 * error * self.inputs[0]
                    # 使用簡化的梯度下降方法更新偏置： 偏置更新量 = 學習率 * 誤差
                    node.bias += 0.0001 * error

                # 更新輸出層 (outLayer) 神經元的權重和偏置
                # 使用簡化的梯度下降方法更新輸出層權重： 權重更新量 = 學習率 * 誤差 * 員工層輸出的總和
                self.outLayer.weight += 0.0001 * error * sum(self.firstOutput)
                # 使用簡化的梯度下降方法更新輸出層偏置： 偏置更新量 = 學習率 * 誤差
                self.outLayer.bias += 0.0001 * error
                #print(f"Input: {input}, Target: {target}, Output: {self.outputs}, Error: {error}")  # 顯示誤差 (可選，用於觀察訓練過程)

def denormalize(output, max_value=1):
    """
    反正規化輸出值。

    將正規化後的輸出值反轉回原始數值範圍 (這裡的實作只是簡單地乘以 max_value，
    在這個例子中，max_value 預設為 1，所以實際上沒有做反正規化)。
    如果在正規化時使用了特定的縮放方法，則需要相應地實作反正規化邏輯。

    參數:
        output (float): 正規化後的輸出值。
        max_value (float, 可選): 正規化時使用的最大值 (預設為 1)。

    返回:
        float: 反正規化後的輸出值。
    """
    return output * max_value

# 建立 Brain (大腦/神經網路) 物件實例
brain = Brain()

# 定義訓練數據集
dataset = [
    ([100,100,500],[1]),  # 輸入特徵 [100, 100, 500]，目標輸出 [1]
    ([300,400,500],[0]),  # 輸入特徵 [300, 400, 500]，目標輸出 [0]
    ([50,300,400],[1]),   # 輸入特徵 [50, 300, 400]，目標輸出 [1]
    ([1000,500,800],[1]), # 輸入特徵 [1000, 500, 800]，目標輸出 [1]
    ([300,500,400],[0]),  # 輸入特徵 [300, 500, 400]，目標輸出 [0]
]

# 訓練神經網路模型，使用上面定義的數據集
brain.train(dataset)

# 輸入測試信號
brain.input([300,400,500])  # 輸入信號 [300, 400, 500]
# 進行前向傳播，計算輸出
brain.process()
# 取得神經網路的輸出結果
output = brain.output()

# 根據輸出結果判斷 "Pass" 或 "Fail"
if denormalize(output) *100 > 5: # 將反正規化後的輸出值乘以 100，如果大於 5 則判斷為 "Pass"
    print("Pass")
    print(denormalize(output)) # 印出 "Pass" 和反正規化後的輸出值
else:
    print("Fail")
    print(denormalize(output)) # 印出 "Fail" 和反正規化後的輸出值