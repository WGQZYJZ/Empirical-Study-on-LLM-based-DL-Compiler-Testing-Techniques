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

    def forward(self, query, key6, value3, mask, d_k):
        q = query
        qk = torch.matmul(q, key6.transpose(-2, -1)) / math.sqrt(d_k)
        qk = qk + mask
        attn_weight = F.softmax(qk, dim=-1)
        attn_vec = torch.matmul(attn_weight, value3)
        out = self.linear_out(attn_vec)
        return out



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
query = 1

test_inputs = [Q, K, V, mask, query]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear_out'

jit:
'Model' object has no attribute 'linear_out'
'''