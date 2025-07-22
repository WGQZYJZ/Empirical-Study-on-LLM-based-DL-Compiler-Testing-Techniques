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

    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(32, 1, (1, 3), 1, padding=(0, 1), groups=1, bias=False)
        self.conv_t = torch.nn.ConvTranspose2d(1, 32, 4, stride=3, padding=1, groups=1, dilation=1, output_padding=0, bias=False)

    def forward(self, img):
        x = self.conv(img)
        x = self.conv_t(x)
        y = (x > 0)
        z = torch.where(y, x, (x * negative_slope))
        return z




func = Model().to('cuda')



img = torch.randn(1, 32, 64, 64)


test_inputs = [img]

# JIT_FAIL
'''
direct:
name 'negative_slope' is not defined

jit:
name 'negative_slope' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''