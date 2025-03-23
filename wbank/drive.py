from wnet import App
from fungpt.deep import DataSets, Brain
from fungpt.models.datasets import ImageFinder

app = App(apiKey="key-here")

class DriveModel(Brain):
    self.layersCount = 189
    self.ds = DataSets(ImageFinder(target="Road&highway&traffic&human", src=["browser/Chrome","browser/Bing","fungpt/images"]), usingNode=128)
    def forward(self):
        return self._forward()
    def imageLook(self):
        result = self._think(self.ds)
        # _think()是訓練 == train
        # _think()會返回概率 (0.0 - 1.0)
        if result >= 0.5:
            pass
        else:
            pass