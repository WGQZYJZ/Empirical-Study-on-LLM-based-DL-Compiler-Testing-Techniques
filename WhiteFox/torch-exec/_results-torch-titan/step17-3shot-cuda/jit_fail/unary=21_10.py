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
        self.conv = torch.nn.Conv2d(1, 2, 3, stride=1)
        self.conv2 = torch.nn.Conv2d(21, 12, 7, padding=13)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv2(v1)
        return torch.tanh(v2)




func = ModelTanh().to('cuda')



x = torch.randn(1, 1, 3, 7)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 21, 7, 7], expected input[1, 2, 1, 5] to have 21 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1, 5)),), **{}):
Given groups=1, weight of size [12, 21, 7, 7], expected input[1, 2, 1, 5] to have 21 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''