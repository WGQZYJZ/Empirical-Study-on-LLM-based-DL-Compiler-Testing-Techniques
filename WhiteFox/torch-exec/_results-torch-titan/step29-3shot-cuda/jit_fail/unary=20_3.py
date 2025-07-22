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
        self.conv_transpose0 = torch.nn.ConvTranspose2d(40, 40, kernel_size=3, stride=2, padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(in_channels=10, out_channels=10, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(in_channels=20, out_channels=20, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(in_channels=10, out_channels=10, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(in_channels=30, out_channels=30, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose5 = torch.nn.ConvTranspose2d(in_channels=10, out_channels=10, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose6 = torch.nn.ConvTranspose2d(in_channels=40, out_channels=40, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)
        self.conv_transpose7 = torch.nn.ConvTranspose2d(in_channels=10, out_channels=10, kernel_size=3, stride=2, padding=1, output_padding=1, dilation=2, groups=1, bias=True)

    def forward(self, x1):
        v1 = self.conv_transpose0(x1)
        v2 = self.conv_transpose1(v1)
        v3 = self.conv_transpose2(v2)
        v4 = self.conv_transpose3(v3)
        v5 = self.conv_transpose4(v4)
        v6 = self.conv_transpose5(v5)
        v7 = self.conv_transpose6(v6)
        v8 = self.conv_transpose7(v7)
        v9 = torch.sigmoid(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 40, 43, 72)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 10, 3, 3], expected input[1, 40, 87, 145] to have 10 channels, but got 40 channels instead

jit:
Failed running call_module L__self___conv_transpose1(*(FakeTensor(..., device='cuda:0', size=(1, 40, 87, 145)),), **{}):
Given transposed=1, weight of size [10, 10, 3, 3], expected input[1, 40, 87, 145] to have 10 channels, but got 40 channels instead

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''