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

    def forward(self, q, k, v, inv_scale_factor=1.0, dropout_p=0.0):
        query = self.query_proj(q)
        key = self.key_proj(k)
        value = self.value_proj(v)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)


func = Model().to('cpu')

w = 32
h = 32

c = 32
b = 8
q = torch.randn(1, b, c, h // 4, w // 4)
w = 32
h = 32

c = 32
b = 8
k = torch.randn(1, b, c, h // 4, w // 4)
w = 32
h = 32

c = 32
b = 8
v = torch.randn(1, b, c, h // 4, w // 4)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'query_proj'

jit:
'Model' object has no attribute 'query_proj'
'''