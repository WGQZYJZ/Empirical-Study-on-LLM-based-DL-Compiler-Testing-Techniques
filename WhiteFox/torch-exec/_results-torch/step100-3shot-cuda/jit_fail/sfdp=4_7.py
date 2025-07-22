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

    def forward(self, q5, k, v, m4):
        Q0 = q5.transpose(1, 2)
        K = k.transpose(1, 2)
        V = v.transpose(1, 2)
        qk = Q0 @ K.transpose(-2, -1) / math.sqrt(Q0.size(-1))
        qk = qk + m4
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ V
        return output



func = Model().to('cuda')


q = torch.randn(1, 64, 56, 56)

k = torch.randn(1, 64, 56, 56)

v = torch.randn(1, 64, 56, 56)

m = torch.rand(1, 56, 56)
m = torch.rand(1, 56, 56)
mask = (m > 0.7).fill_(-1000000000.0)

test_inputs = [q, k, v, m, mask]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 6 were given

jit:
forward() takes 5 positional arguments but 6 were given
'''