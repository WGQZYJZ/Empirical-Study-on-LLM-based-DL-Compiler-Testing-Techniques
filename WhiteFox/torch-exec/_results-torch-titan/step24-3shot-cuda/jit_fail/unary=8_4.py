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

    def forward(self, x1):
        t1 = torch.nn.functional.interpolate(x1, mode='bilinear', align_corners=False)
        x2 = torch.relu(t1)
        t3 = x2.clone()
        v4 = torch.nn.functional.interpolate(t3, size=[64], mode='bilinear', align_corners=False)
        v5 = (x2 / v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
either size or scale_factor should be defined

jit:
Failed running call_function <function interpolate at 0x7b6821377430>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)),), **{'mode': 'bilinear', 'align_corners': False}):
either size or scale_factor should be defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''