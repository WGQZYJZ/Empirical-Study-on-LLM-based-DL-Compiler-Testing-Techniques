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

    def __init__(self, dim, num_heads, dropout_p):
        super().__init__()
        self.W_q = torch.nn.Linear(dim, dim)
        self.W_k = torch.nn.Linear(dim, dim)
        self.W_v = torch.nn.Linear(dim, dim)
        self.W_o = torch.nn.Linear(dim, dim)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, query, key, value):
        q = self.W_q(query)
        k = self.W_k(key)
        v = self.W_v(value)
        scale_factor = torch.sqrt(torch.tensor(key.size((- 1))))
        q = q.div(scale_factor)
        qk = torch.matmul(q, torch.transpose(k, (- 2), (- 1)))
        softmax_qk = qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, v)
        output = self.W_o(output)
        return output



dim = 1
num_heads = 1
dropout_p = 1

func = Model(dim, num_heads, dropout_p).to('cuda')



query = torch.rand(1, 8, 64, 64)



key = torch.rand(1, 8, 64, 64)



value = torch.rand(1, 8, 64, 64)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (512x64 and 1x1)

jit:
Failed running call_module L__self___W_q(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
a and b must have same reduction dim, but got [512, 64] X [1, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''