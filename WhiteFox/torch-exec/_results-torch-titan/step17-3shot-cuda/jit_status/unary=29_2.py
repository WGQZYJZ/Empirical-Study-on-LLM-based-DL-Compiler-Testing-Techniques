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

    def __init__(self, min_value=(- 1.3), max_value=3.3):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.act_3 = torch.nn.ReLU6()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x5):
        v4 = self.conv_transpose2d(x5)
        v6 = torch.clamp_min(v4, self.min_value)
        v7 = torch.clamp_max(v6, self.max_value)
        v9 = self.act_3(v7)
        return v9




func = Model().to('cuda')



x5 = torch.randn(1, 3, 3, 3)


test_inputs = [x5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppez2q61f/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppez2q61f', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppez2q61f/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''