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

    def __init__(self, min_value=(2.701 + 1e-06), max_value=(2.999 - 1e-06)):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 5, 5, stride=1, padding=2)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(5, 8, 3, stride=2, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(8, 32, 4, stride=2, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(32, 128, 5, stride=4, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv_transpose1(v1)
        v3 = self.conv_transpose2(v2)
        v4 = self.conv_transpose3(v3)
        v5 = v4.clamp(self.min_value, self.max_value)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 63, 63)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp69smzw_e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp69smzw_e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp69smzw_e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''