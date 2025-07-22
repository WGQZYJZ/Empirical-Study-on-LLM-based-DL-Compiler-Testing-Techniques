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

class MyModel(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, q, k, v, mask=None):
        q = q / dim ** (-0.5)
        dot_product = torch.matmul(q, k.transpose(-2, -1))
        if mask is not None:
            dot_product.mul_(mask)
        attention = torch.softmax(dot_product, dim=-1)
        output = torch.matmul(attention, v)
        return output


dim = 1
func = MyModel(4096).to('cpu')


q = torch.randn(100, 1024)

k = torch.randn(100, 4096)

v = torch.randn(100, 4096)

mask = torch.zeros(100, 4096, 4096)

test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x1024 and 4096x100)

jit:
Failed running call_function <built-in method matmul of type object at 0x795f94d96ec0>(*(FakeTensor(..., size=(100, 1024)), FakeTensor(..., size=(4096, 100))), **{}):
a and b must have same reduction dim, but got [100, 1024] X [4096, 100].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''