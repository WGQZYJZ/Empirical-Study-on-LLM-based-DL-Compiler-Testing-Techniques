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
        self.conv2d = torch.nn.Conv2d(16, 16, 3, stride=1, padding=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 4, 3, stride=(- 1), padding=0)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 + 3)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 16, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 16, 130, 130)),), **{}):
non-positive stride is not supported

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''