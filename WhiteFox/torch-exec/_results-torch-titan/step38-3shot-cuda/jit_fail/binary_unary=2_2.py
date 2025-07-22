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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(12, 24, 4, stride=4, padding=0)
        self.conv2 = torch.nn.Conv2d(24, 12, 5)
        self.conv2.bias.data = self.conv1.bias.data

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = (v1 - 0.5)
        v4 = (v2 - v3)
        v5 = F.gelu(v4)
        v6 = (v5 - v4)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 12, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given weight of size [12, 24, 5, 5], expected bias to be 1-dimensional with 12 elements, but got bias of size [24] instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 24, 8, 8)),), **{}):
Given weight of size [12, 24, 5, 5], expected bias to be 1-dimensional with 12 elements, but got bias of size [24] instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''