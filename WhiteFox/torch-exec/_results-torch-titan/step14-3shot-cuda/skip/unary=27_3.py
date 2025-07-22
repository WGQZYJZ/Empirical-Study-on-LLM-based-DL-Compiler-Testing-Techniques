import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__():
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 128, 1, stride=1, padding=1)
        self.avgpool = torch.nn.AvgPool2d(2)

    def forward(self, x):
        x_1 = self.conv(x)
        x_2 = torch.clamp_max(x_1, 0.5)
        x_3 = self.avgpool(x_2)
        x_4 = torch.clamp_min(x_3, (- 0.5))
        x_5 = self.avgpool(x_2)
        x_6 = torch.clamp_min(x_5, (- 1.0))
        return x_4




func = Model().to('cuda')



x = torch.randn(2, 3, 64, 64)


test_inputs = [x]
