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

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, inv_scale_factor, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


dropout_p = 1
func = Model(0.5).to('cpu')


query = torch.randn(3, 512, 128)

key = torch.randn(3, 512, 128)

value = torch.randn(3, 512, 128)

inv_scale_factor = torch.randn(3)

test_inputs = [query, key, value, inv_scale_factor]

# JIT_FAIL
'''
direct:
The size of tensor a (512) must match the size of tensor b (128) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., size=(s0, s4, s1)), FakeTensor(..., size=(3, 512, 128))), **{}):
The size of tensor a (s1) must match the size of tensor b (128) at non-singleton dimension 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''