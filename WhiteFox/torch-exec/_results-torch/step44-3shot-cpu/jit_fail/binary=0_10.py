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
        self.input = torch.randn(1, 1, 1, 1, requires_grad=True)
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(16, 1, 1, stride=1, padding=0)

    def forward(self):
        v1 = self.conv1(self.input)
        v2 = self.conv2(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 16, 28, 28)

x2 = torch.randn(3, 1, 28, 28)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 3 were given

jit:
forward() takes 1 positional argument but 3 were given
'''