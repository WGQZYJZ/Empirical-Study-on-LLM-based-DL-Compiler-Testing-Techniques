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

    def forward(self, value, key, query, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)


func = Model().to('cpu')


value = torch.randn(8, 1, 25, 64)

key = torch.randn(8, 1, 25, 64)

query = torch.randn(8, 1, 25, 64)

inv_scale_factor = torch.randn(8)
dropout_p = 1

test_inputs = [value, key, query, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (25) must match the size of tensor b (8) at non-singleton dimension 3

jit:
Failed running call_method div(*(FakeTensor(..., size=(8, 1, 25, 25)), FakeTensor(..., size=(8,))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([8]); but expected shape should be broadcastable to [8, 1, 25, 25]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''