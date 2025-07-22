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

    def __init__(self, size, dropout=0.0):
        super().__init__()
        self.size = size
        self.dropout = dropout
        self.dropout_module = torch.nn.Dropout(dropout)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.div(float(self.size) ** (-0.5))
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = self.dropout_module(v3)
        v5 = torch.matmul(v3, x2)
        return (v4, v5)


size = 1

func = Model(size).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x = torch.randn(20, 16)

test_inputs = [x1, x2, x]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''