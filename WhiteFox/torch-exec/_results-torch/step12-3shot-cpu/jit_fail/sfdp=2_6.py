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
        self.query = torch.nn.Parameter(torch.randn(1, 64, 32, 32))
        self.key = torch.nn.Parameter(torch.randn(1, 32, 64, 64))
        self.value = torch.nn.Parameter(torch.randn(1, 32, 64, 64))
        self.inv_scale_factor = torch.nn.Parameter(torch.randn(32, 32))
        self.dropout_p = 0.8

    def forward(self, x2):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value)
        return output


func = Model().to('cpu')


x2 = torch.randn(1, 1, 64, 64)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x76c671196ec0>(*(Parameter(FakeTensor(..., size=(1, 64, 32, 32), requires_grad=True)), FakeTensor(..., size=(1, 32, 64, 64), requires_grad=True)), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''