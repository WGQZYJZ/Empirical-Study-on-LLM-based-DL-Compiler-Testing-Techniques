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
        super(Model, self).__init__()

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = query.matmul(key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor.unsqueeze(-1).unsqueeze(-1))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cpu')


query = torch.randn(2, 5, 2, 6)

key = torch.randn(2, 4, 5, 6)

value = torch.randn(2, 4, 2, 6)

inv_scale_factor = torch.randn(2, 2)
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(s0, s1, s2, s3)), FakeTensor(..., size=(s4, s5, s7, s6))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''