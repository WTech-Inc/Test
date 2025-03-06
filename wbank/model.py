import numpy as np

class NeuralNode:
    def __init__(self, weight=0, bias=0):
        self.weight = weight if weight is not None else np.random.rand() * 0.001  # 權重
        self.bias = bias if bias is not None else np.random.rand() * 0.001   # 偏置

    def sigmoid(self, z):
        # Sigmoid 函數
        return 1 / (1 + np.exp(-z))

    def compute(self, inputs):
        # 計算加權求和 + 偏置
        weighted_sum = sum(i * self.weight for i in inputs) + self.bias
        return weighted_sum
        # 使用 Sigmoid 激活函數
        #return self.sigmoid(weighted_sum)

class Brain:
    def __init__(self):
        self.staff = [NeuralNode() for _ in range(3)]  # 員工list
        self.outLayer = NeuralNode()
    def normalize(self, inputs):
        max_values = [40, 30000, 150000]  # 根據數據集的最大值設置
        normalized = []
        for x, max_val in zip(inputs, max_values):
            if max_val == 0:
                normalized.append(0)  # 防止除以零
            else:
                normalized.append(x / max_val)
        return normalized
    def input(self, inputs):
        self.inputs = self.normalize(inputs)
    def process(self):
        # 對每個神經元計算輸出
        self.firstOutput = [ node.compute(self.inputs) for node in self.staff]
        self.outputs = self.outLayer.compute(self.firstOutput)

    def output(self):
        return self.outputs
    def train(self, dataset, epochs=100):
        for _ in range(epochs):
          for input, target in dataset:
            self.input(input)
            self.process()
            for i ,  node in enumerate(self.staff):
                error = target[0] - self.outputs
                node.weight += 0.00001 * error * self.inputs[i]
                node.bias += 0.00001 * error
                self.outLayer.weight += 0.00001 * error * sum(self.firstOutput)
                self.outLayer.bias += 0.00001 * error
                #print(f"Input: {input}, Target: {target}, Output: {self.outputs}, Error: {error}")  # 顯示誤差

def denormalize(output, max_value=1):
    return output * max_value

brain = Brain()

dataset = [
    ([18,10000,40000],[40000]),
    ([18,10000,100000],[0]),
    ([18,14500,34000],[0]),
    ([18,20000,10000],[10000]),
    ([18,20000,15000],[15000]),
    ([18,25000,20000],[20000]),
    ([18,20000,150000],[28000]),
    ([24,30000,80000],[33000]),
]

# 訓練model
brain.train(dataset)

brain.input([18,9000,100000])  # 輸入信號
brain.process()
output = brain.output()
prediectAmount = denormalize(output)
print(f"{prediectAmount:.2f}")
print(f"每月還款: {prediectAmount/12:.2f}")