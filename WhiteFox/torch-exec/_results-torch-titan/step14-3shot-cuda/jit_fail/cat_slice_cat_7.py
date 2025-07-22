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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        out1 = self.conv1(x1)
        out2 = self.conv2(out1)
        c1 = torch.nn.functional.interpolate(out2, scale_factor=2, mode='trilinear', align_corners=None)
        c2 = torch.cat([c1, out2], dim=1)
        c3 = c2[:, 100:200]
        c4 = torch.cat([c1, c3], dim=1)
        return c4



func = Model().to('cuda')



x1 = torch.randn(1, 3, 96, 96)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Got 4D input, but trilinear mode needs 5D input

jit:
Failed running call_function <function interpolate at 0x7a897e9f7430>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 100, 100)),), **{'scale_factor': 2, 'mode': 'trilinear', 'align_corners': None}):
Got 4D input, but trilinear mode needs 5D input

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''