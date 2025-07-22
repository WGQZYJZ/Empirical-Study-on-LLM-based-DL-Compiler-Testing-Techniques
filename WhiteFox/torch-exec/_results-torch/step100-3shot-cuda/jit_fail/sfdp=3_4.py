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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


scale_factor = 1
dropout_p = 1
func = Model(scale_factor, dropout_p).to('cuda')


query = torch.randn(1, 3, 128, 128)

key = torch.randn(1, 64, 128, 128)

value = torch.randn(1, 64, 128, 128)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7c9476396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)), FakeTensor(..., device='cuda:0', size=(1, 64, 128, 128))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''