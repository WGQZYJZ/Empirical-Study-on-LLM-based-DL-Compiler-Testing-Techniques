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

    def __init__(self, dim, num_heads, batch_size, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.softmax_qk = torch.nn.Softmax(dim=-1)
        self.dropout_qk = torch.nn.Dropout(self.dropout_p)
        self.matmul1 = torch.nn.Linear(dim, 1)
        self.matmul2 = torch.nn.Linear(dim, 1, bias=False)

    def forward(self, query, key, value, scale_factor, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = self.dropout_qk(softmax_qk)
        return (torch.matmul(dropout_qk, value), dropout_qk)


dim = 64
num_heads = 2
batch_size = [2, 4]
dropout_p = 0.2

func = Model(dim, num_heads, batch_size, dropout_p).to('cpu')

query = 1
key = 1
value = 1
scale_factor = 1
inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
AttributeError: 'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''