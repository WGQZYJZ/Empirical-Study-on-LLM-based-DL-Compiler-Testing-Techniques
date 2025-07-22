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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 16, 1, stride=1)
        self.conv_2 = torch.nn.Conv2d(1, 32, 1, stride=1)

    def forward(self, x1):
        x2 = self.conv_1(x1)
        x2 = torch.tanh(x2)
        x2 = self.conv_2(x2)
        return x2




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 3, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 1, 1, 1], expected input[1, 16, 100, 100] to have 1 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv_2(*(FakeTensor(..., device='cuda:0', size=(1, 16, 100, 100)),), **{}):
Given groups=1, weight of size [32, 1, 1, 1], expected input[1, 16, 100, 100] to have 1 channels, but got 16 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''