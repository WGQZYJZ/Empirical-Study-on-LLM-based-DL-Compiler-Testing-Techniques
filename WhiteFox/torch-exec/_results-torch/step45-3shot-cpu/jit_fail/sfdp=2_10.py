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

class M(torch.nn.Module):

    def __init__(self, query, key, value, dropout_p, inv_scale_factor):
        super().__init__()

    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(self, softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)
        return output


query = 1
key = 1
value = 1
dropout_p = 0.2
inv_scale_factor = 8.0

func = M(query, key, value, dropout_p, inv_scale_factor).to('cpu')


q1 = torch.randn(5, 16, 64, 64)

k1 = torch.randn(5, 16, 64, 64)

v1 = torch.randn(5, 16, 64, 64)

test_inputs = [q1, k1, v1]

# JIT_FAIL
'''
direct:
'M' object has no attribute 'inv_scale_factor'

jit:
'M' object has no attribute 'inv_scale_factor'
'''