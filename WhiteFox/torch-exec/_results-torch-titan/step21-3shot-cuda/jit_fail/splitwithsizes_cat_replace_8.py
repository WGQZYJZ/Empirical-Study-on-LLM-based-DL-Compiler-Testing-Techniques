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
        self.features = torch.nn.Conv2d(3, 32, 3, 1, 1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, 1, 1)
        self.maxpool = torch.nn.AvgPool2d(3, 3, 3)

    def forward(self, v1):
        out = self.features(v1)
        out = self.conv2(out)
        out = self.maxpool(out)
        out = out.view(1, (- 1))
        return (out, torch.split(v1, 64, 1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=3 and kernel_size=3

jit:
Failed running call_module L__self___maxpool(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)),), **{}):
pad should be at most half of kernel size, but got pad=3 and kernel_size=3

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''