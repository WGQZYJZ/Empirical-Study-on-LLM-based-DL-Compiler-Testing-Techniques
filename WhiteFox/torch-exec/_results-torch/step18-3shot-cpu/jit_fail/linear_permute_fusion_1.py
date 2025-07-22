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
        v4 = x1
        v1 = torch.nn.functional.conv2d(v4, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return v2



func = Model().to('cpu')


x1 = torch.randn((1, 2, 2, 2))

test_inputs = [x1]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e60b7196ec0>(*(FakeTensor(..., size=(1, 2, 2, 2)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
expected stride to be a single integer value or a list of 0 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''