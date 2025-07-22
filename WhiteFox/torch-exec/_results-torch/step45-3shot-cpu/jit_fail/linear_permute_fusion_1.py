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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3, x4):
        v3 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        v4 = v3.permute(0, 2, 1)
        v6 = torch.nn.functional.linear(x4, self.linear.weight, self.linear.bias)
        v7 = v6.permute(0, 2, 1)
        v1 = x1
        v2 = torch.nn.functional.linear(x3, self.linear.weight, self.linear.bias)
        v5 = v2.permute(1, 0, 2, 3)
        v8 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v5 + v4 + v7 + v8



func = Model().to('cpu')


x1 = torch.randn(2, 1, 2)

x2 = torch.randn(1, 2, 2, 2, device='cpu')

x3 = torch.randn(1, 2, 2, 2, device='cpu')

x4 = torch.randn(1, 2, 2, 2, device='cpu')

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 2, 2, 2)), 0, 2, 1), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''