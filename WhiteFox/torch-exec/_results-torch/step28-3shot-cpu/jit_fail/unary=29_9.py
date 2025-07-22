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

    def __init__(self, min_value=11, max_value=5.8):
        super().__init__()
        self.interpolate = torch.nn.Upsample(scale_factor=2, mode='linear')
        self.conv = torch.nn.Conv2d(3, 10, 1, stride=1)
        self.max_pool2d = torch.nn.MaxPool2d(10, stride=1, padding=2)
        self.act_1 = torch.nn.ReLU6()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, input):
        v3 = self.interpolate(input)
        v4 = self.conv(v3)
        v6 = self.max_pool2d(v4)
        v7 = self.act_1(v6)
        v9 = torch.clamp_min(v7, self.min_value)
        v10 = torch.clamp_max(v9, self.max_value)
        return v10



func = Model().to('cpu')


input = torch.randn(1, 3, 112, 112)

test_inputs = [input]

# JIT_FAIL
'''
direct:
Got 4D input, but linear mode needs 3D input

jit:
Got 4D input, but linear mode needs 3D input
'''