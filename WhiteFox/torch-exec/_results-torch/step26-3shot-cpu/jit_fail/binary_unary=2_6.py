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
        self.conv1 = torch.nn.Conv2d(32, 1, kernel_size=5, stride=2, padding=0)
        self.conv2 = torch.nn.Conv2d(32, 32, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = v1 - v2
        v4 = F.relu(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 32, 10, 10)

x2 = torch.randn(1, 32, 20, 20)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''