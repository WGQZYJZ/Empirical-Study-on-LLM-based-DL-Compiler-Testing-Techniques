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

    def __init__(self, d_in, d_out):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(d_in, d_out) / d_in ** 0.5)
        self.key = torch.nn.Parameter(torch.randn(d_in, d_out) / d_in ** 0.5)
        self.value = torch.nn.Parameter(torch.randn(d_in, d_out) / d_in ** 0.5)
        self.scale_factor = d_in ** 0.5
        self.dropout_p = 0.1

    def forward(self, x1):
        qk = torch.matmul(x1, self.key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output


d_in = 1
d_out = 1

func = Model(d_in, d_out).to('cpu')


x1 = torch.randn(1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (64x64 and 1x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x721f52d96ec0>(*(FakeTensor(..., size=(1, 64, 64)), FakeTensor(..., size=(1, 1), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [64, 64] X [1, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''