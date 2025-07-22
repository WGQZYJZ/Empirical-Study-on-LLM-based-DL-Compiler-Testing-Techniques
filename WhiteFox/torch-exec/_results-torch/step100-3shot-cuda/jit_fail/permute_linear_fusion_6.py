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
        self.relu6 = torch.nn.ReLU6()
        self.relu6.training = False
        self.linear = torch.nn.Linear(4, 16)
        self.transpose = torch.transpose
        self.matmul = torch.matmul

    def forward(self, x1):
        v1 = self.relu6(x1)
        v1 = v1.to(self.linear.weight.dtype)
        v1 = self.transpose(v1, -2, -1)
        v1 = self.matmul(v1, self.linear.weight)
        return v1



func = Model().to('cuda')


x1 = torch.randn(1, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x1 and 16x4)

jit:
Failed running call_function <built-in method matmul of type object at 0x7a9dbab96ec0>(*(FakeTensor(..., device='cuda:0', size=(4, 1)), Parameter(FakeTensor(..., device='cuda:0', size=(16, 4), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 1] X [16, 4].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''