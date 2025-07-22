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
        self.negative_slope = 0.5
        self.conv_t = torch.nn.ConvTranspose2d(1, 7, 7, stride=2, padding=0, output_padding=1, bias=True)
        self.conv = torch.nn.Conv2d(7, 21, 1, stride=1, bias=True)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = (v1 * self.negative_slope)
        v3 = torch.relu(v2)
        v4 = self.conv(v3)
        v5 = (v4 > 0)
        v6 = (v4 * (- 1.42))
        v7 = torch.where(v5, v4, v6)
        return v7




func = Model().to('cuda')



x = torch.randn(4, 1, 224, 224, device='cuda')


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq2nw62mj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpq2nw62mj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpq2nw62mj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''