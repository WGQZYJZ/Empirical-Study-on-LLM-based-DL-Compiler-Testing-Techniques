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
        self.key = torch.nn.Parameter(torch.randn(8))

    def forward(self, x1):
        query = x1.softmax(dim=0)
        k = x1 + x1.transpose(-2, -1)
        v = x1 + x1.transpose(-2, -1)
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(query, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.argmax(dim=-1)
        output = attention_weights * x1
        return output



func = Model().to('cpu')


x1 = torch.randn(8, 64, 64, requires_grad=False)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, s1), dtype=torch.int64), FakeTensor(..., size=(s0, s1, s1))), **{}):
The size of tensor a (s0) must match the size of tensor b (s1) at non-singleton dimension 1)

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''