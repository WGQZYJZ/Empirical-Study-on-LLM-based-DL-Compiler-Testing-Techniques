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
        self.conv1 = torch.nn.Conv2d(3, 5, 3, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(5, affine=False)

    def forward(self, x1):
        y1 = self.conv1(x1)
        y2 = self.bn1(y1)
        y3 = self.conv1(y2)
        return y3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [5, 3, 3, 3], expected input[1, 5, 3, 3] to have 3 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 5, 3, 3)),), **{}):
Given groups=1, weight of size [5, 3, 3, 3], expected input[1, 5, 3, 3] to have 3 channels, but got 5 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''