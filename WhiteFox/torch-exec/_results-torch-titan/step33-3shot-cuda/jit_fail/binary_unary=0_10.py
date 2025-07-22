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
        self.conv1 = torch.nn.Conv2d(2, 8, 7)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.layer_wrapper(v1)
        return v2

    def layer_wrapper(self, x):
        v3 = self.conv1(x)
        return v3




func = Model().to('cuda')



x = torch.randn(1, 2, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 2, 7, 7], expected input[1, 8, 58, 58] to have 2 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 58, 58)),), **{}):
Given groups=1, weight of size [8, 2, 7, 7], expected input[1, 8, 58, 58] to have 2 channels, but got 8 channels instead

from user code:
   File "<string>", line 23, in forward
  File "<string>", line 27, in layer_wrapper


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''