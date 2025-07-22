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

    def __init__(self, hidden_size, num_heads, num_features):
        super().__init__()
        self.scale_factor = (hidden_size ** (- 0.5))
        self.dropout = torch.nn.Dropout(p=0.0)
        self.q = torch.nn.Linear(num_features, num_features, bias=False)
        self.k = torch.nn.Linear(num_features, num_features, bias=False)
        self.v = torch.nn.Linear(num_features, num_features, bias=False)

    def forward(self, query, key, value, dropout_p=0.1):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        max_dim = scaled_qk.shape[(- 1)]
        dropout_qk = self.dropout(scaled_qk.softmax(dim=(- 1)).to(torch.float64))
        dropout_qk = torch.nn.functional.dropout(dropout_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output




hidden_size = 32


num_heads = 4


num_features = 128

func = Model(hidden_size, num_heads, num_features).to('cuda')



hidden_size = 32


query = torch.randn(4, 20, hidden_size)



hidden_size = 32


key = torch.randn(4, 40, hidden_size)

value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (80x32 and 128x128)

jit:
Failed running call_module L__self___q(*(FakeTensor(..., device='cuda:0', size=(4, 20, 32)),), **{}):
a and b must have same reduction dim, but got [80, 32] X [128, 128].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''