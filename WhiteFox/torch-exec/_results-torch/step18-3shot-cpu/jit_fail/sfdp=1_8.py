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

    def __init__(self, d_model):
        super(Model, self).__init__()
        self.q = torch.nn.Linear(d_model, d_model, bias=False)
        self.k = torch.nn.Linear(d_model, d_model, bias=False)
        self.v = torch.nn.Linear(d_model, d_model, bias=False)
        self.scale_factor = d_model ** (-0.5)
        self.atten_dropout = torch.nn.Dropout(0.1)

    def forward(self, q, k, v):
        q = self.q(q)
        k = self.k(k)
        v = self.v(v)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * self.scale_factor
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        atten_dropout_qk = self.atten_dropout(softmax_qk)
        output = torch.matmul(atten_dropout_qk, v)
        return output


d_model = 1
func = Model(512).to('cpu')


q = torch.randn(3, 10, 512)

k = torch.randn(2, 10, 512)

v = torch.randn(2, 10, 512)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x778ca2396ec0>(*(FakeTensor(..., size=(3, 10, 512)), FakeTensor(..., size=(2, 512, 10))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''