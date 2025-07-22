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
        self.linear = torch.nn.Linear(784, 512)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = torch.sigmoid(torch.tanh(v2))
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (28x28 and 784x512)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s1, s0)), Parameter(FakeTensor(..., size=(512, 784), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s1, s0] X [784, 512].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''