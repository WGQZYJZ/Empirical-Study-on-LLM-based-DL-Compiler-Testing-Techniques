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

    def __init__(self, input_size=128):
        super().__init__()
        self.query = torch.nn.Linear(input_size, input_size)
        self.key = torch.nn.Linear(input_size, input_size)
        self.value = torch.nn.Linear(input_size, input_size)

    def forward(self, query, key, value, scale_factor, dropout_p):
        q = self.query(query)
        k = self.key(key)
        v = value
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model(128).to('cuda')



query = torch.randn(8, 128, 2)



key = torch.randn(8, 256, 2)



value = torch.randn(8, 256, 2)

scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1024x2 and 128x128)

jit:
Failed running call_module L__self___query(*(FakeTensor(..., device='cuda:0', size=(8, 128, 2)),), **{}):
a and b must have same reduction dim, but got [1024, 2] X [128, 128].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''