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
        v1 = self.linear.bias
        v2 = self.linear.weight
        v3 = (v1 + v2)
        x2 = v1.permute(0, 2, 1)
        v3 = (v3 + x2)
        v3 = v3.permute(0, 2, 1)
        x3 = (x1 + v3)
        v4 = torch.rand(2, 2)
        x4 = (x1 * v2)
        x3 = (x4 - x1)
        x2 = (x3 + 1)
        return x2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 1 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True)), 0, 2, 1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 2)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''