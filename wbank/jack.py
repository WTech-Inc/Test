"""
  pip install jcimporter deepfun
"""
"""
jcimporter init && jcimporter install-get jc-body jc-head jc-brain deepfun-ext
"""

from deepfun.models import FunBrain
from jc.services import system

device = system.usb.findFirstDevice()
device.modelName = "Jack"

device.datasets.feed(FunBrain)
device.fit(trainingTime=100)

device.run()