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
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cpu')


k = torch.randn(1, 32, 32, 1)

q = torch.randn(1, 16, 8, 1)

v = torch.randn(1, 32, 8, 1)

test_inputs = [k, q, v]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7f0cc8f96ec0>(*(FakeTensor(..., size=(1, 32, 32, 1)), FakeTensor(..., size=(1, 16, 1, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''