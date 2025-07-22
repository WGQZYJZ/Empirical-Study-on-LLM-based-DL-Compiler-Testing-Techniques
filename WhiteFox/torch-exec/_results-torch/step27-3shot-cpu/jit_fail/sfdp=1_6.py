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

    def __init__(self, num_channels, dropout_p, num_heads, q_dim, kv_dim, scale_factor):
        super().__init__()

    def forward(self, x1, x2):
        x3 = torch.nn.functional.normalize(x2)
        x4 = torch.matmul(x1, x3.transpose(-2, -1))
        x6 = torch.div(x4, self.scale_factor)
        x7 = torch.nn.functional.softmax(x6, dim=-1)
        x8 = torch.nn.functional.dropout(x7, p=self.dropout_p)
        x9 = torch.matmul(x8, self.v)
        return x9


num_channels = 1
dropout_p = 1
num_heads = 1
q_dim = 1
kv_dim = 1
scale_factor = 1

func = Model(num_channels, dropout_p, num_heads, q_dim, kv_dim, scale_factor).to('cpu')


x1 = torch.randn(1, 16, 8, 8)

x2 = torch.randn(1, 16, 8, 8)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'scale_factor'

jit:
'Model' object has no attribute 'scale_factor'
'''