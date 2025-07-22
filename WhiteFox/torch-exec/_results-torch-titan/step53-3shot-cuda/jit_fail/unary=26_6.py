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



class Conv3DBias(torch.nn.Conv3d):

    def __init__(self, in_channels, bias):
        super(Conv3DBias, self).__init__(in_channels, in_channels, 3, stride=1, padding=1, dilation=1)
        self.input_bias = bias

    def forward(self, input):
        return (F.conv3d(input, self.weight, self.bias) + self.input_bias)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_t = Conv3DBias(2, 1)

    def forward(self, x1):
        x2 = torch.sum(x1, dim=3)
        x3 = self.conv_t(x2)
        return x3




func = Model().to('cuda')



x1 = torch.randn(4, 2, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
Failed running call_function <built-in method sum of type object at 0x75d60a4699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 2, 3)),), **{'dim': 3}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''