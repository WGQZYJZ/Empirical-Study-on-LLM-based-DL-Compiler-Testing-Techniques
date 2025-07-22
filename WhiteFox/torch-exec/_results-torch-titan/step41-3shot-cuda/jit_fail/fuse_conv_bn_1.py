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
        a = torch.nn.Conv2d(2, 3, 1)
        torch.manual_seed(3)
        a.weight = torch.nn.Parameter(torch.randn(a.weight.shape))
        self.conv = torch.nn.Conv2d(2, 3, 1)
        torch.manual_seed(7)
        self.conv.weight = torch.nn.Parameter(torch.randn(self.conv.weight.shape))
        self.fc = torch.nn.Linear(32, 10)
        torch.manual_seed(8)
        self.fc.weight = torch.nn.Parameter(torch.randn(self.fc.weight.shape))
        torch.manual_seed(9)
        self.fc.bias = torch.nn.Parameter(torch.randn(self.fc.bias.shape))

    def forward(self, x1):
        v0 = F.interpolate(self.conv(x1), mode='linear', align_corners=False)
        v1 = F.avg_pool2d(v0, kernel_size=7, stride=7, padding=0, ceil_mode=False, count_include_pad=True)
        v2 = torch.flatten(v1, 1)
        v3 = self.fc(v2)

    def forward(self, x1):
        v0 = F.interpolate(self.conv(x1), mode='linear', align_corners=False)
        v1 = F.avg_pool2d(v0, kernel_size=7, stride=7, padding=0, ceil_mode=False, count_include_pad=True)
        ret = self.fc(v1)
        return ret




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
either size or scale_factor should be defined

jit:
Failed running call_function <function interpolate at 0x7859952b7430>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{'mode': 'linear', 'align_corners': False}):
either size or scale_factor should be defined

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''