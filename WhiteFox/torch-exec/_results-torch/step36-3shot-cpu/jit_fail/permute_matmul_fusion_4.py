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

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).squeeze(-1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.nn.functional.conv2d(v2, v1)
        return v3.squeeze(-1)



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 2)

x2 = torch.randn(1, 2, 4, 4)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 4 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 1, s0, s1)), 0, 2, 1), **{}):
Attempting to permute a tensor of rank 4, but received a permutation of length 3!

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''