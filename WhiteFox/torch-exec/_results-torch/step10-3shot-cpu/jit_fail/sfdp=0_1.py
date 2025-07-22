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
        self.query = torch.nn.Parameter(torch.randn(8))
        self.key = torch.nn.Parameter(torch.randn(8, 64))

    def forward(self, x2):
        q = self.query
        k = self.key
        v = x2
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output



func = Model().to('cpu')


x2 = torch.randn(1, 8, 64, 64)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x8 and 64x8)

jit:
Failed running call_function <built-in method matmul of type object at 0x7bf966196ec0>(*(Parameter(FakeTensor(..., size=(8,), requires_grad=True)), FakeTensor(..., size=(64, 8), requires_grad=True)), **{}):
a and b must have same reduction dim, but got [1, 8] X [64, 8].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''