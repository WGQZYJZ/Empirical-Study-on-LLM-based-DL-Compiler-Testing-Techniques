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

    def forward(self, query, key, value, scale_factor, dropout_p, mask):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = scaled_qk.div(scale_factor)
        softmax_qk = torch.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.drop_out(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 2, 8, 16)

key = torch.randn(1, 2, 16, 32)

value = torch.randn(1, 2, 16, 32)

scale_factor = torch.randn(1, 128)

mask = torch.randn(1, 1, 16, 16)
dropout_p = 1

test_inputs = [query, key, value, scale_factor, mask, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 16] but got: [2, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7b9fa4f96ec0>(*(FakeTensor(..., size=(1, 2, 8, 16)), FakeTensor(..., size=(1, 2, 32, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 16] but got: [2, 32].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''