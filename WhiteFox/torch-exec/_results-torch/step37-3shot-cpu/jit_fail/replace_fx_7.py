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

class m1(torch.nn.Module):

    def __init__(self, m2):
        super().__init__()
        self.m2 = m2
        self.c1 = torch.nn.Conv2d(3, 4, 5)

    def forward(self, x1):
        x2 = torch.randint(0, 10, (1,))
        x3 = x1 ** x2
        x4 = self.m2.forward(x3)
        x5 = self.m2(x3)
        x6 = self.c1(x3)
        x7 = x6 * x4 - x4
        x8 = torch.randint(0, 10, (1,))
        x9 = x2 + x8
        x10 = x9.view(-1)
        x11 = len(x10)
        x12 = self.c1.groups // x8
        x13 = self.c1.bias
        x14 = x13.view(x12, 3, 4)
        x15 = self.m2.p2.shape[0]
        x16 = self.m2.p3.shape[0]
        return torch.add(x12, x15)

class m2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.p1 = torch.rand(1)
        self.p2 = torch.nn.Parameter(torch.randn(1))

    def forward(self, x1):
        x2 = x1.permute(2, 3, 1, 0)
        x3 = torch.transpose(x2, -1, -2)
        x4 = torch.nn.functional.dropout(x1)
        x5 = x1 ** self.p1.item()
        x6 = torch.nn.functional.dropout(x5)
        x7 = torch.nn.functional.dropout(x5)
        x8 = torch.rand_like(x5)
        x9 = torch.randint(0, 10, (1,))
        x10 = self.p2 + x5 + x6
        x11 = self.p2
        return x10



func = m2().to('cpu')


x1 = torch.randn(1, 3, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 3 is not equal to len(dims) = 4

jit:
Failed running call_method permute(*(FakeTensor(..., size=(1, 3, 4)), 2, 3, 1, 0), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 46, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''