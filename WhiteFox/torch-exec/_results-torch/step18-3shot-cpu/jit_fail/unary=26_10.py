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
        self.conv_t = torch.nn.ConvTranspose2d(480, 12, 2, stride=2, groups=12)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = x2.flatten()
        x4 = x3 > 0
        x5 = x3 * 0.5
        x6 = torch.where(x4, x3, x5)
        x7 = x6.reshape(x6.size(0), 12, 12, 12)
        return x7 + torch.nn.functional.adaptive_avg_pool2d(x7, (2, 2)) + torch.nn.functional.unfold(x7, kernel_size=2, stride=2, padding=0)



func = Model().to('cpu')


x1 = torch.randn(4, 480, 10, 10)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[19200, 12, 12, 12]' is invalid for input of size 19200

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(48*s0*s1*s2,)), 48*s0*s1*s2, 12, 12, 12), **{}):
shape '[48*s0*s1*s2, 12, 12, 12]' is invalid for input of size 48*s0*s1*s2

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''