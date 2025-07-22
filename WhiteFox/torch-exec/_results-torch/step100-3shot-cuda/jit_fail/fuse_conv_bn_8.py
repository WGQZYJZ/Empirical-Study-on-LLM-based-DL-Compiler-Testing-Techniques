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
        torch.manual_seed(2)
        self.conv1 = torch.nn.Conv1d(3, 3, 3)
        self.block = torch.nn.Sequential(torch.nn.BatchNorm1d(3), torch.nn.ReLU())

    def forward(self, x2):
        y1 = self.conv1(x2)
        y2 = self.block(y1)
        return y2

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.block = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.Conv2d(7, 3, 1))

    def forward(self, x):
        return self.block(x)



func = Model().to('cuda')


x2 = torch.randn(1, 3, 10)

x = torch.randn(1, 7, 10, 10)

test_inputs = [x2, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''