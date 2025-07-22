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
        v2 = x1 + v1
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.permute(1, 0, 2)
        v4 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v5 = v3.unsqueeze(dim=0) * v2.unsqueeze(dim=0)
        v5 = v5
        v5 = v5 + torch.eye(v5.shape[-1])[None, ...]
        v5 = v5 + 2
        v5 = torch.tanh(v5)
        v5 = v5.permute(1, 0, 2)
        v5 = v5.squeeze(dim=-1)
        v5 = v4 / v1
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 2, 2, 2)), 1, 0, 2), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''