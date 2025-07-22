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
        v1 = x2.permute(0, 2, 1)
        v2 = torch.tensor(42)
        v2 = v2.permute(0, 2, 1)
        v3 = torch.tensor(43)
        v3 = v3.permute(0, 1, 2)
        v4 = torch.bmm(x1, v1)
        v4 = v4.permute(1, 2, 0)
        return v2



func = Model().to('cpu')


x1 = torch.randn(2, 2, 2)

x2 = torch.randn(2, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 0 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(), dtype=torch.int64), 0, 2, 1), **{}):
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 0 is not equal to len(dims) = 3

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''