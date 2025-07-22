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
        self.w = torch.randn(6)
        self.w = torch.nn.Parameter(self.w)

    def forward(self, x2):
        v1 = torch.matmul(x2, self.w)
        v2 = torch.sigmoid(v1)
        return v2


func = Model().to('cpu')


x2 = torch.randn(1, 64)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
size mismatch, got input (1), mat (1x64), vec (6)

jit:
Failed running call_function <built-in method matmul of type object at 0x7da083196ec0>(*(FakeTensor(..., size=(1, 64)), Parameter(FakeTensor(..., size=(6,), requires_grad=True))), **{}):
size mismatch, got input (1x64), vec (6)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''