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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3((v1 + v2))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)



x2 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 8, 32, 32] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)),), **{}):
Given groups=1, weight of size [8, 3, 3, 3], expected input[1, 8, 32, 32] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''