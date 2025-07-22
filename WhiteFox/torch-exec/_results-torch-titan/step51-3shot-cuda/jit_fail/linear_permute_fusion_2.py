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
        self.conv2d = torch.nn.Conv2d(2, 2, 1)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = v1.permute(0, 2, 1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(4, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 2, 1, 1], expected input[1, 4, 2, 2] to have 2 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(4, 2, 2)),), **{}):
Given groups=1, weight of size [2, 2, 1, 1], expected input[1, 4, 2, 2] to have 2 channels, but got 4 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''