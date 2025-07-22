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

    def forward(y, self, query, key, value, attn_mask=0.0):
        return y(self(query, key, value, attn_mask), query, key, value, attn_mask)



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
self = 1

test_inputs = [Q, K, V, mask, self]

# JIT_FAIL
'''
direct:
'Tensor' object is not callable

jit:
'Tensor' object is not callable
'''