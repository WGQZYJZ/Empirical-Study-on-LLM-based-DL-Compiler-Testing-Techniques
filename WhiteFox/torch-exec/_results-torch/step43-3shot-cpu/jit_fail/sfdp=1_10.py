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
        self.dropout_p = 0.5
        self.attn = torch.nn.MultiheadAttention(8, 2, dropout=self.dropout_p)

    def forward(self, x1, x2):
        v1 = self.attn(x1, x2)
        return v1


func = Model().to('cpu')


x1 = torch.randn(16, 8, 64)

x2 = torch.randn(16, 16, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() missing 1 required positional argument: 'value'

jit:
forward() missing 1 required positional argument: 'value'
'''