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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(5, 8, 128)

key = torch.randn(5, 8, 128)

value = torch.randn(6, 8, 128)

inv_scale_factor = torch.randn(6, 8, 8)
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (6) at non-singleton dimension 0

jit:
Failed running call_method div(*(FakeTensor(..., size=(5, 8, 8)), FakeTensor(..., size=(s0, 8, 8))), **{}):
The size of tensor a (5) must match the size of tensor b (s0) at non-singleton dimension 0)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''