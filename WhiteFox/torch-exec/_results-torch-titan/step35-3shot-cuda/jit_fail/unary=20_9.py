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
        self.deconvs = torch.nn.Sequential(torch.nn.ConvTranspose2d(3, 2, 5, stride=1, padding=2, output_padding=1), torch.nn.ConvTranspose2d(3, 1, kernel_size=2, stride=2, padding=1, output_padding=1), torch.nn.Sigmoid())

    def forward(self, x):
        return self.deconvs(x)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
Failed running call_module L__self___deconvs_1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 17, 17)),), **{}):
Given transposed=1, weight of size [3, 1, 2, 2], expected input[1, 2, 17, 17] to have 3 channels, but got 2 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''