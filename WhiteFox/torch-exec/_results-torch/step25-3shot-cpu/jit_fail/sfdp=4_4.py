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
        self.attn = torch.nn.MultiheadAttention(8, 8)

    def forward(self, x1, x2):
        (v1, v2) = self.attn(x1, x2, x2)
        return v1


func = Model().to('cpu')


x1 = torch.randn(1, 32, 8)

x2 = torch.randn(1, 16, 8)

x4 = torch.randn(32, 16)

x5 = torch.randn(1, 16, 8)

test_inputs = [x1, x2, x4, x5]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 5 were given

jit:
forward() takes 3 positional arguments but 5 were given
'''