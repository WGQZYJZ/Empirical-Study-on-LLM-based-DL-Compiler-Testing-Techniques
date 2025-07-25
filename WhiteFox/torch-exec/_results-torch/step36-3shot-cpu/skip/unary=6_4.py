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

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, 10, stride=1, padding=1, groups=10)
        self.bn = torch.nn.BatchNorm2d(10)

    def forward(self, x1):
        x1 = self.conv(x1)
        x2 = 3 + x1
        x3 = torch.clamp_min(x2, 0)
        x4 = torch.clamp_max(x3, 6)
        x5 = x1 * x4
        x6 = x5 / 6
        x7 = self.bn(x6)
        return x7



func = Model().to('cpu')


x_1 = torch.randn(2, 3, 256, 256)

test_inputs = [x_1]
