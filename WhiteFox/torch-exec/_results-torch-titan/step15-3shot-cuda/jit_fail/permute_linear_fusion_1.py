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
        self.sigmoid = torch.nn.Sigmoid()
        self.conv = torch.nn.Conv2d(1, 1, (1, 1))

    def forward(self, x1):
        x1 = self.sigmoid(x1)
        x1 = self.conv(x1).permute(2, 0, 3, 1)
        x1 = x1.reshape(1, 2)
        return x1




func = Model().to('cuda')



x1 = torch.randn([1, 2, 2, 1])


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 2, 2, 1] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 1)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 2, 2, 1] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''