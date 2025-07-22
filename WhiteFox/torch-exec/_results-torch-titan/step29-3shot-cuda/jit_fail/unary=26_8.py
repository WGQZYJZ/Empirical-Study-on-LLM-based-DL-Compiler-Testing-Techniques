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
        self.conv_t1 = torch.nn.ConvTranspose2d(30, 20, 3, stride=1, padding=1, output_padding=1)
        self.conv_t2 = torch.nn.ConvTranspose2d(10, 20, 2, stride=2)
        self.conv_t3 = torch.nn.ConvTranspose2d(20, 10, 3, stride=2, padding=1, output_padding=1)
        self.conv_t4 = torch.nn.ConvTranspose2d(10, 5, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x11):
        t1 = self.conv_t1(x11)
        t2 = (t1 > 0)
        t3 = (t1 * 1)
        t4 = torch.where(t2, t1, t3)
        t5 = self.conv_t2(t4)
        t6 = (t5 > 0)
        t7 = (t5 * 1)
        t8 = torch.where(t6, t5, t7)
        t9 = self.conv_t3(t8)
        t10 = (t9 > 0)
        t11 = (t9 * 1)
        t12 = torch.where(t10, t9, t11)
        t13 = self.conv_t4(t12)
        t14 = (t13 > 0)
        t15 = (t13 * 1)
        t16 = torch.where(t14, t13, t15)
        return t16




func = Model().to('cuda')



x11 = torch.randn(6, 30, 224, 224)


test_inputs = [x11]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
Failed running call_module L__self___conv_t2(*(FakeTensor(..., device='cuda:0', size=(6, 20, 225, 225)),), **{}):
Given transposed=1, weight of size [10, 20, 2, 2], expected input[6, 20, 225, 225] to have 10 channels, but got 20 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''