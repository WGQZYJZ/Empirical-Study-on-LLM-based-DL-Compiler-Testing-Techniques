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

    def __init__(self, min_value=False, max_value=False):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.conv2d = torch.nn.Conv2d(4, 1, 1, stride=1, padding=0, dilation=1)
        self.max_value = max_value
        self.min_value = min_value

    def forward(self, x):
        y = torch.clamp_min(x, self.min_value)
        y = torch.clamp_max(y, self.max_value)
        y = self.conv2d(y)
        y = self.relu(y)
        return y




func = Model().to('cuda')



x = torch.randn(1, 4, 513, 512)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpuni6lgv3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpuni6lgv3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpuni6lgv3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''