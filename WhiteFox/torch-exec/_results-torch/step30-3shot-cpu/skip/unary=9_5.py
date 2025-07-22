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
        self.conv = torch.nn.Conv2d(10, 8, 3, stride=3, padding=2, dilation=2, groups=10)
        self.other_conv = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1, groups=10)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 2 + v1
        v3 = v2.clamp(min=0, max=6)
        v4 = v3 / 6
        v5 = self.other_conv(v4)
        v6 = 3 + v5
        v7 = v6.clamp(min=0, max=6)
        v8 = v7 / 6
        return v8



func = Model().to('cpu')


x1 = torch.randn(5, 10, 256, 256)

test_inputs = [x1]
