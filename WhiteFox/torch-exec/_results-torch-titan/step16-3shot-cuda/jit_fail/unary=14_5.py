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
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0, bias=True)
        self.conv2 = torch.nn.Conv2d(16, 16, 4, stride=2, padding=1, bias=True)
        self.conv3 = torch.nn.Conv2d(16, 128, 2, stride=2, padding=1, bias=True)
        self.convT_1 = torch.nn.ConvTranspose2d(304, 16, 6, stride=2, padding=1, output_padding=1, dilation=2, bias=True)
        self.convT_2 = torch.nn.ConvTranspose2d(176, 64, 5, stride=2, padding=1, output_padding=1, dilation=2, bias=True)
        self.convT_3 = torch.nn.ConvTranspose2d(128, 4, 7, stride=3, padding=1, output_padding=1, dilation=2, bias=True)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        t3 = self.conv3(t2)
        t5 = torch.cat([t2, t3], dim=1)
        x = self.convT_1(t5)
        x = self.convT_2(x)
        x = self.convT_3(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(2, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 4, 4], expected input[2, 3, 256, 256] to have 16 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(2, 3, 256, 256)),), **{}):
Given groups=1, weight of size [16, 16, 4, 4], expected input[2, 3, 256, 256] to have 16 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''