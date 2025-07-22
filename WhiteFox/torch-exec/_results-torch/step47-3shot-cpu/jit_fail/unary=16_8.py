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

    def __init__(self, input_channels, input_size):
        super().__init__()
        self.linear = torch.nn.Linear(input_size ** 2 * input_channels, input_size ** 2)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.relu(v1)
        return v2


input_channels = 1
input_size = 1

func = Model(input_channels, input_size).to('cpu')


x = torch.randn(1, 3, 64, 64)
x = torch.randn(1, 3, 64, 64)
x = torch.randn(1, 3, 64, 64)
y = x.view(x.size(0), -1)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''