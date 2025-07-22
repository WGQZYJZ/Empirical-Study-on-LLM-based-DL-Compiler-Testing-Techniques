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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3, affine=False)

    def forward(self, x):
        s = self.conv1(x)
        y = self.bn(s)
        return y




func = Model().to('cuda')



x = torch.randn(1, 512, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 512, 32, 32] to have 3 channels, but got 512 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 512, 32, 32)),), **{}):
Given groups=1, weight of size [3, 3, 3, 3], expected input[1, 512, 32, 32] to have 3 channels, but got 512 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''