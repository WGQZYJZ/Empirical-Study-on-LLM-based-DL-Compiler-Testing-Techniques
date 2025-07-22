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
        self.conv1 = torch.nn.Conv2d(2, 1, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 9, 1, stride=1, padding=1)

    def forward(self, x1, conv_weight=None, conv_bias=None, other=1, x2=None):
        var1 = self.conv1(x1)
        if (not (None in (conv_weight, conv_bias))):
            var1 = torch.nn.functional.linear(var1, conv_weight, conv_bias)
        var2 = self.conv2(var1)
        if (not (None in (conv_weight, conv_bias))):
            var2 = torch.nn.functional.linear(var2, conv_weight, conv_bias)
        v2 = (var2 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(4, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 4, 4, 4] to have 2 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(4, 4, 4)),), **{}):
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 4, 4, 4] to have 2 channels, but got 4 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''