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
        self.key = torch.nn.Parameter(torch.randn(4, 3, 3))

    def forward(self, x1):
        q = x1
        k = x1.reshape(-1, 3)
        v = x1
        inv_scale = math.sqrt(k.size(1))
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output



func = Model().to('cpu')


x1 = torch.randn(1, 4, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 3]' is invalid for input of size 16384

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(1, s0, s1, s2)), -1, 3), **{}):
shape '[-1, 3]' is invalid for input of size s0*s1*s2

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''