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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = torch.addmm(x1, self.linear.weight, self.linear.bias)
        v2 = v1.unsqueeze(dim=0)
        v3 = torch.cat([v2], dim=0)
        return v3


func = Model().to('cuda')


x1 = torch.randn(8, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x736dbdd96ec0>(*(FakeTensor(..., device='cuda:0', size=(8, 3)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''