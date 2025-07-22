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

    def __init__(self, block_count=3, output_channel_count=32):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, int((output_channel_count / 2)), 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, output_channel_count, 1, stride=1, padding=1)
        self.conv_blocks = []
        for _ in range(3):
            self.conv_blocks.append(torch.nn.Sequential(torch.nn.BatchNorm2d(output_channel_count), torch.nn.ReLU(), torch.nn.Conv2d(output_channel_count, output_channel_count, 1, stride=1, padding=1), torch.nn.ReLU(), torch.nn.Conv2d(output_channel_count, output_channel_count, 1, stride=1, padding=1), torch.nn.BatchNorm2d(output_channel_count), torch.nn.ReLU(), torch.nn.Conv2d(output_channel_count, output_channel_count, 1, stride=1, padding=1)))

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(x)
        for i in range(3):
            v11 = self.conv_blocks[i](v1)
            v12 = self.conv_blocks[i](v2)
            v1 = (v1 + v11)
            v2 = (v2 + v12)
        return (v1 + v2)



func = Model().to('cuda')



x = torch.randn(1, 3, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 16 elements not 32

jit:
Failed running call_module self___conv_blocks_0_0(*(FakeTensor(..., device='cuda:0', size=(1, 16, 258, 258)),), **{}):
running_mean should contain 16 elements not 32

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''