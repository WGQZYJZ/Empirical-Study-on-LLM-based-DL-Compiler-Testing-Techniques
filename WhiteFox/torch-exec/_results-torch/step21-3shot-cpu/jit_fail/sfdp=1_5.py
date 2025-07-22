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

    def __init__(self, query, key, value, inv_scale_factor, dropout_p):
        super().__init__()

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


query = 1
key = 1
value = 1
inv_scale_factor = 1
dropout_p = 1

func = Model(query, key, value, inv_scale_factor, dropout_p).to('cpu')


x1 = torch.randn(16, 32, 16)

x2 = torch.randn(16, 32, 24)

x3 = torch.randn(16, 32, 24)
query = 1
key = 1

test_inputs = [x1, x2, x3, query, key]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 16] but got: [16, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d4cef196ec0>(*(FakeTensor(..., size=(16, 32, 16)), FakeTensor(..., size=(16, 24, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 16] but got: [16, 24].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''