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
        self.conv1 = torch.nn.Conv2d(3, 3, kernel_size=2, stride=1)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.softmax = torch.nn.Softmax(dim=3)
        self.conv2 = torch.nn.Conv2d(3, 3, kernel_size=1, stride=1, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(3)
        self.max_pool_2d = torch.nn.MaxPool2d(2, stride=2)

    def forward(self, x1):
        a = self.softmax(x1)
        v1 = a + x1 * a
        v1 = self.bn1(self.conv1(v1))
        v1 = v1 + x1
        v2 = self.conv2(self.max_pool_2d(v1))
        v2 = v2 * a
        v3 = v2 + self.bn2(self.max_pool_2d(v1))
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6)

x2 = torch.randn(1, 3, 6, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''