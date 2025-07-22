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
        self.linear = torch.nn.Linear(in_features=64, out_features=1024, bias=True)

    def forward(self, x4):
        v7 = self.linear(x4)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8



func = Model().to('cpu')

x4 = 1

test_inputs = [x4]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''