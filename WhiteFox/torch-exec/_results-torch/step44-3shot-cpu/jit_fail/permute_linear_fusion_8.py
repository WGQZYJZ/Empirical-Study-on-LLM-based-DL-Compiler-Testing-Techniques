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
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 1), stride=(1, 1), padding=(0,), dilation=(1,))

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = v2 * 2
        v3 = v2.unsqueeze(1)
        v4 = self.conv(v3)
        v5 = v4.squeeze(1)
        v6 = v2 + v5
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x1 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, s0, s1, 1)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [s0*s1, 1] X [2, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''