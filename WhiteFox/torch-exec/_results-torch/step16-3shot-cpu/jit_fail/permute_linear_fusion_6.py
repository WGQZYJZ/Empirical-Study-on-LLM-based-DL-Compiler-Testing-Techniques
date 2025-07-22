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

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.nn.functional.tanh(v1)
        v4 = v3 * x2
        v4 = v4 + v2
        v5 = x2.permute(1, 0)
        v5 = torch.nn.functional.linear(v5, self.linear.weight, self.linear.bias)
        v6 = torch.nn.functional.tanh(v1)
        v7 = v6.transpose(1, 1)
        v8 = x2.permute(1, 0)
        v9 = v8.transpose(1, 1)
        v10 = torch.nn.functional.linear(v7, v9, None)
        v3 = torch.matmul(x2, v10)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 3 is not equal to len(dims) = 2

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 2, 2)), 1, 0), **{}):
Attempting to permute a tensor of rank 3, but received a permutation of length 2!

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''