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

    def forward(self, query, key, value, inv_scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


__input_tensor__ = torch.randn(1, 10, 10)

q = torch.randn(1, 4, 10)

k = torch.randn(1, 5, 10)

v = torch.randn(1, 6, 10)

test_inputs = [__input_tensor__, q, k, v]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (10) at non-singleton dimension 2

jit:
Failed running call_method div(*(FakeTensor(..., size=(1, 10, 4)), FakeTensor(..., size=(1, 6, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 6, 10]); but expected shape should be broadcastable to [1, 10, 4]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''