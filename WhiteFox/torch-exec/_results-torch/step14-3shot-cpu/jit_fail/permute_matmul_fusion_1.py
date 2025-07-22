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
        super(Model, self).__init__()

    def forward(self, x1, x2):
        v3 = torch.matmul(x1.permute(0, 2, 1), x2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(25)

x2 = torch.randn(3, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 1 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., size=(25,)), 0, 2, 1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 2)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''