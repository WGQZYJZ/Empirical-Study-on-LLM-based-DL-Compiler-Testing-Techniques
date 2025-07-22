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
        self.conv_t_0 = torch.nn.Conv2d(128, 64, 3, stride=1, padding=1)
        self.relu_0 = torch.nn.ReLU()
        self.conv_t_1 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, output_padding=0)
        self.relu_1 = torch.nn.ReLU()
        self.conv_t_2 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, output_padding=1)
        self.relu_2 = torch.nn.ReLU()
        self.conv_t_3 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1, output_padding=0)
        self.relu_3 = torch.nn.ReLU()
        self.conv_t_4 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, output_padding=0)
        self.relu_4 = torch.nn.ReLU()
        self.conv_t_5 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1, output_padding=1)
        self.relu_5 = torch.nn.ReLU()
        self.conv_t_6 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1, output_padding=1)
        self.relu_6 = torch.nn.ReLU()
        self.conv_t_7 = torch.nn.ConvTranspose2d(64, 1, 3, stride=1, padding=1)
        self.relu_7 = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv_t_0(x1)
        v2 = self.relu_0(v1)
        v3 = self.conv_t_1(v2)
        v4 = self.relu_1(v3)
        v5 = self.conv_t_2(v3)
        v6 = self.relu_2(v5)
        v7 = self.conv_t_3(v5)
        v8 = self.relu_3(v7)
        v9 = self.conv_t_4(v7)
        v10 = self.relu_4(v9)
        v11 = self.conv_t_5(v9)
        v12 = self.relu_5(v11)
        v13 = self.conv_t_6(v11)
        v14 = self.relu_6(v13)
        v15 = self.conv_t_7(v14)
        v16 = self.relu_7(v15)
        v17 = v15
        return v17



func = Model().to('cpu')


x1 = torch.randn(1, 128, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp52up_fbc/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp52up_fbc/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp52up_fbc', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''