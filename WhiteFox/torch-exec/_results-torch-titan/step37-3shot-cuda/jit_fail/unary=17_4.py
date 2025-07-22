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
        self.conv = torch.nn.ConvTranspose2d(16, 16, 3, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.nn.functional.interpolate(v2, None, None, 1.5, 'nearest')
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
either size or scale_factor should be defined

jit:
Failed running call_function <function interpolate at 0x7bdbb8278430>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)), None, None, 1.5, 'nearest'), **{}):
either size or scale_factor should be defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''