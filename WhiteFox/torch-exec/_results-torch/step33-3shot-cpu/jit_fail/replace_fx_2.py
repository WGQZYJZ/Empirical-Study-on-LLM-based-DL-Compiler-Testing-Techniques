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

class Module0(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv0_weight = torch.nn.Parameter(torch.randn([1, 3, 3, 3]))

    def forward(self, x1):
        x2 = F.conv2d(x1, self.conv0_weight)
        return x2



func = Module0().to('cpu')


x1 = torch.randn(1, 1, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 3, 3, 3], expected input[1, 1, 4, 4] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x745402f96ec0>(*(FakeTensor(..., size=(1, 1, 4, 4)), Parameter(FakeTensor(..., size=(1, 3, 3, 3), requires_grad=True))), **{}):
Given groups=1, weight of size [1, 3, 3, 3], expected input[1, 1, 4, 4] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''