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
        self.conv = torch.nn.Conv2d(224, 128, 1, stride=2)
        self.maxpool = torch.nn.MaxPool2d(2, stride=2, padding=0)

    def forward(self, t1):
        v1 = self.conv(t1)
        v2 = (v1 - torch.transpose(t1, 2, 1))
        v3 = F.relu(v2)
        v4 = (v3 - self.maxpool(t1))
        v5 = F.relu(v4)
        return v5




func = Model().to('cuda')



t1 = torch.randn(1, 3, 224, 224)


test_inputs = [t1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 224, 1, 1], expected input[1, 3, 224, 224] to have 224 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 224, 224)),), **{}):
Given groups=1, weight of size [128, 224, 1, 1], expected input[1, 3, 224, 224] to have 224 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''