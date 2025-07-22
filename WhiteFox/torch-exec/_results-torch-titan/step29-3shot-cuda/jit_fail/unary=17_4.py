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



class Model(nn.Module):

    def __init__(self, model_op, kernel_op, pad_op, bias_op, stride_op, in_channels_op, out_channels_op, kernel_size_op):
        super(Model, self).__init__()
        self.kernel_op = kernel_op
        self.pad_op = pad_op
        self.stride_op = stride_op
        self.out_channels_op = out_channels_op
        self.conv = nn.ConvTranspose2d(in_channels_op, out_channels_op, kernel_size_op, (stride_op, 4), (1, pad_op), bias_op)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.relu(v1)
        return v2



model_op = 1
kernel_op = 1
pad_op = 1
bias_op = 1
stride_op = 1
in_channels_op = 1
out_channels_op = 1
kernel_size_op = 1

func = Model(model_op, kernel_op, pad_op, bias_op, stride_op, in_channels_op, out_channels_op, kernel_size_op).to('cuda')



x1 = torch.randn(1, 2048, 7, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 1, 1], expected input[1, 2048, 7, 7] to have 1 channels, but got 2048 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2048, 7, 7)),), **{}):
Given transposed=1, weight of size [1, 1, 1, 1], expected input[1, 2048, 7, 7] to have 1 channels, but got 2048 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''