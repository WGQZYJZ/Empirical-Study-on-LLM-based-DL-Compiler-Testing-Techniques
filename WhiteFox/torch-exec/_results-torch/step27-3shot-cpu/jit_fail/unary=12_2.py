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
        self.conv1 = torch.nn.Conv2d(16, 5, 5, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(self.conv1.out_channels)
        self.pool = torch.nn.MaxPool2d(2, 2, padding=1)
        self.conv2 = torch.nn.Conv2d(5, 10, 5, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.relu(v1)
        v3 = v2.flatten()
        v4 = self.bn(v3)
        v5 = v4.reshape(1)
        v6 = v5.sigmoid()
        v7 = self.pool(v1)
        v8 = self.conv2(v7)
        v9 = F.relu(v8)
        v10 = self.pool(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected 4D input (got 1D input)

jit:
expected 4D input (got 1D input)
'''