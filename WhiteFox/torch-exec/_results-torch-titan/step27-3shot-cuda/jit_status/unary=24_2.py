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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(24, 62, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(62, 28, 3, stride=2, padding=2)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(v4)
        v6 = (v5 > 0)
        v7 = (v5 * (- 0.1))
        v8 = torch.where(v6, v5, v7)
        return v8




negative_slope = 0.03


func = Model(negative_slope).to('cuda')



x1 = torch.randn(1, 24, 20, 20)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6l7w0hj5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6l7w0hj5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6l7w0hj5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''