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

    def __init__(self, dropout=0.1, ntoken=30000, ninp=768):
        super().__init__()
        self.drop = torch.nn.Dropout(dropout)
        self.embedding = torch.nn.Embedding(ntoken, ninp)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.matmul = torch.matmul

    def forward(self, query, key, value, scale_factor):
        qk = self.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.drop(softmax_qk)
        output = self.matmul(dropout_qk, value)
        return output


func = Model(dropout=0.4, ntoken=30000, ninp=768).to('cpu')


query = torch.randn(10, 3, 768)

key = torch.randn(10, 3, 768)

value = torch.randn(10, 3, 768)

scale_factor = torch.randn(10)

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (10) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., size=(s0, s4, s1)), FakeTensor(..., size=(10,))), **{}):
The size of tensor a (s1) must match the size of tensor b (10) at non-singleton dimension 2)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''