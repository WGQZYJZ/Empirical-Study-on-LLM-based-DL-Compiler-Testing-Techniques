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
        self.conv = torch.nn.Conv2d(3, 3, kernel_size=1)
        self.conv2 = torch.nn.Conv2d(3, 3, kernel_size=1)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 2, 1)
        v3 = x1
        v2 = torch.nn.functional.conv2d(v1, self.conv.weight, self.conv.bias)
        v3 = v3.permute(0, 3, 2, 1)
        v3 = torch.nn.functional.conv2d(v3, self.conv2.weight, self.conv2.bias)
        return (v2, v3)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 2, 2, 3] to have 3 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f3cf0996ec0>(*(FakeTensor(..., size=(1, 2, 2, 3)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True))), **{}):
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 2, 2, 3] to have 3 channels, but got 2 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''