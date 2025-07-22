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
        self.conv = torch.nn.Conv2d(64, 3, 4, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)

    def forward(self, x):
        v1 = self.conv2(self.conv(x)) > 0
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 64, 112, 112)

x2 = torch.randn(1, 64, 112, 112)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''