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
        self.conv = torch.nn.Conv2d(12, 13, 2, stride=2)
        self.conv2 = torch.nn.Conv2d(11, 14, 1, stride=1, padding=1)

    def forward(self, x):
        x = self.conv(x)
        x = torch.tanh(x)
        return self.conv2(x)




func = Model().to('cuda')



x = torch.randn(1, 12, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [14, 11, 1, 1], expected input[1, 13, 16, 16] to have 11 channels, but got 13 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 13, 16, 16)),), **{}):
Given groups=1, weight of size [14, 11, 1, 1], expected input[1, 13, 16, 16] to have 11 channels, but got 13 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''