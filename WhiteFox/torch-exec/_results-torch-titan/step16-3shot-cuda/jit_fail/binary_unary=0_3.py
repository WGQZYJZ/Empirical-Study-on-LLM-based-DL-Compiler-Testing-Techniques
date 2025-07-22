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
        self.conv = torch.nn.Conv2d(3, 3, 7, stride=1, padding=3)

    def forward(self, x, y, z):
        v1 = self.conv(x)
        v2 = self.conv(v1)
        v3 = (v2 + y)
        v4 = torch.relu(v3)
        v5 = self.conv(v1)
        v6 = (v5 + z)
        return (v4 + v6)




func = Model().to('cuda')



x = torch.randn(1, 2, 3, 3)



y = torch.randn(1, 3, 3, 3)



z = torch.randn(1, 1, 3, 3)


test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 7, 7], expected input[1, 2, 3, 3] to have 3 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)),), **{}):
Given groups=1, weight of size [3, 3, 7, 7], expected input[1, 2, 3, 3] to have 3 channels, but got 2 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''