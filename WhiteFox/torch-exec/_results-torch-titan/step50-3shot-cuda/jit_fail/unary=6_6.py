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
        self.batch_norm3d = torch.nn.BatchNorm3d(num_features=36, eps=1e-05, momentum=0.1)
        self.conv = torch.nn.Conv3d(1, 1, 1)

    def forward(self, x1):
        t1 = self.batch_norm3d(x1)
        t2 = self.conv(t1)
        t3 = (t1 + t2)
        t4 = torch.clamp(t3, 0, 6)
        t5 = (t3 - t4)
        return t5




func = Model().to('cuda')



x1 = torch.randn(2, 36, 128, 128, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1, 1], expected input[2, 36, 128, 128, 64] to have 1 channels, but got 36 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 36, 128, 128, 64)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1, 1], expected input[2, 36, 128, 128, 64] to have 1 channels, but got 36 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''