

import torch
from torchvision import models
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._net = torch.nn.Sequential()
 
        for m in list(models.vgg19().features)[:-4]:
            self._net.add_module('0' + str(len(m)),  # pylint: disable=protected-access
                m)

        self._net.add_module("0012",  # pylint: disable=protected-access
            torch.nn.AvgPool2d(kernel_size=(3, 3), stride=1))
 
        for i in range(4):
            for j in range(5):
                self._net.add_module("0{}1{}".format(i + 1, j),
                    torch.nn.Conv2d(in_channels=64 if (
                        i < 3 or ((j == 1) and (i > 1))) else
                    512, out_channels=self._net[-8].out_channels // 8,
                        kernel_size=(3, 3), stride=1, padding=0))
 
 
    def forward(self, x):
        v = self. _net(x)
 
        return torch.nn.functional.adaptive_avg_pool2d(v[None], (7, 7))
 
 
model = Model()

