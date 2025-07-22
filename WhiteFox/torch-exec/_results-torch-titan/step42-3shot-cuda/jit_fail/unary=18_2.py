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
        self.conv = torch.nn.Conv2d(12, 24, 9, padding=4)
        self.avgpool = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.maxpool = torch.nn.MaxPool2d(4, stride=4)
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = self.avgpool(v1)
        v1 = self.maxpool(v1)
        v1 = self.gelu(v1)
        t1 = v1.view(v1.shape[0], (- 1), v1.shape[2], v1.shape[3], v1.shape[4], v1.shape[5]).squeeze()
        return t1




func = Model().to('cuda')



x1 = torch.randn(1, 12, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (24x1x1). Calculated output size: (24x0x0). Output size is too small

jit:
Failed running call_module L__self___maxpool(*(FakeTensor(..., device='cuda:0', size=(1, 24, 1, 1)),), **{}):
Given input size: (24x1x1). Calculated output size: (24x0x0). Output size is too small

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''