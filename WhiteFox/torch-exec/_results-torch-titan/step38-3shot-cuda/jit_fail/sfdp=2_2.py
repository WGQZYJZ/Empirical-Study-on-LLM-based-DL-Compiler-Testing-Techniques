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

    def __init__(self, num_queries, num_keys, num_values, num_heads=8, scale_factor=1.0, dropout_p=0.0):
        super().__init__()
        self.num_heads = num_heads
        self.scale_factor = (scale_factor / (num_heads ** 0.5))
        self.dropout_p = dropout_p
        self.matmul1 = torch.nn.Linear(in_features=num_queries, out_features=(num_heads * num_keys), bias=False)
        self.matmul2 = torch.nn.Linear(in_features=num_keys, out_features=(num_heads * num_values), bias=False)

    def forward(self, query, key, value):
        matmul1 = self.matmul1(query)
        matmul2 = self.matmul2(key)
        qh = matmul1.view((matmul1.shape[:(- 1)] + (self.num_heads, self.num_keys)))
        kh = matmul2.view((matmul2.shape[:(- 1)] + (self.num_heads, self.num_values)))
        qk = torch.matmul(qh, kh.permute(0, 1, 3, 2))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



num_queries = 1
num_keys = 1
num_values = 1

func = Model(num_queries, num_keys, num_values).to('cuda')



q = torch.randn(2, 32, 512)



k = torch.randn(2, 64, 512)



v = torch.randn(2, 64, 512)


test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x512 and 1x8)

jit:
Failed running call_module L__self___matmul1(*(FakeTensor(..., device='cuda:0', size=(2, 32, 512)),), **{}):
a and b must have same reduction dim, but got [64, 512] X [1, 8].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''