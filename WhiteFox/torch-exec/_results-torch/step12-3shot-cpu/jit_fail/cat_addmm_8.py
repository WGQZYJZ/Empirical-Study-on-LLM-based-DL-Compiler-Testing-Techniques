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
        self.l1 = torch.nn.Linear(3, 8)

    def forward(self, input):
        v1 = torch.addmm(input, self.l1.weight, self.l1.bias)
        outputs = [v1]
        return outputs


func = Model().to('cpu')


input = torch.randn(1, 3)

test_inputs = [input]

# JIT_FAIL
'''
direct:
mat2 must be a matrix, got 1-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x719f52f96ec0>(*(FakeTensor(..., size=(1, 3)), Parameter(FakeTensor(..., size=(8, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True))), **{}):
b must be 2D

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''