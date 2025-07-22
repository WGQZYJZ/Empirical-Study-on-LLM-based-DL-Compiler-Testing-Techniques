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
        self.batch_norm1 = torch.nn.BatchNorm2d(num_features=64, eps=0.05, momentum=0.05)
        self.batch_norm2 = torch.nn.BatchNorm2d(num_features=32, eps=0.01, momentum=0.01)
        self.avg_pool = torch.nn.AdaptiveAvgPool2d((7, 7))

    def forward(self, x7):
        v1 = self.batch_norm1(x7)
        v2 = torch.sigmoid(v1)
        v3 = self.batch_norm2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.avg_pool(v4)
        return v5




func = Model().to('cuda')



x7 = torch.randn(32, 32, 7, 7)


test_inputs = [x7]

# JIT_FAIL
'''
direct:
running_mean should contain 32 elements not 64

jit:
Failed running call_module L__self___batch_norm1(*(FakeTensor(..., device='cuda:0', size=(32, 32, 7, 7)),), **{}):
running_mean should contain 32 elements not 64

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''