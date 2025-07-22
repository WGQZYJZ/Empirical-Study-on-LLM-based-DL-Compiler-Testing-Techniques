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

    def __init__(self, dim, sequence_length, heads, dropout_p):
        super().__init__()
        self.dim = dim
        self.sequence_length = sequence_length
        self.heads = heads
        self.dropout_p = dropout_p
        self.scale_factor = math.sqrt(self.dim)
        self.to_query = torch.nn.Linear(self.dim, self.dim)
        self.to_key = torch.nn.Linear(self.dim, self.dim)
        self.to_value = torch.nn.Linear(self.dim, self.dim)
        self.dropout = torch.nn.Dropout(self.dropout_p)

    def forward(self, query, key, value):
        q = self.to_query(query)
        k = self.to_key(key)
        v = self.to_value(value)
        q *= self.scale_factor
        q = q.view((- 1), self.heads, self.sequence_length, self.dim)
        k = k.view((- 1), self.heads, self.sequence_length, self.dim)
        v = v.view((- 1), self.heads, self.sequence_length, self.dim)
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        output = output.view((- 1), (self.heads * self.sequence_length), self.dim)
        output = self.dropout(output)
        return output



dim = 1
sequence_length = 1
heads = 1
dropout_p = 1

func = Model(dim, sequence_length, heads, dropout_p).to('cuda')



query = torch.randn(1, 20, 32)



key = torch.randn(1, 20, 32)



value = torch.randn(1, 20, 32)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x32 and 1x1)

jit:
Failed running call_module L__self___to_query(*(FakeTensor(..., device='cuda:0', size=(1, 20, 32)),), **{}):
a and b must have same reduction dim, but got [20, 32] X [1, 1].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''