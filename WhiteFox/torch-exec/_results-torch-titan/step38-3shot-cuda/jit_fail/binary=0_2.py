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
        self.conv1 = torch.nn.Conv2d(4, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 4, 1, stride=1, padding=1)

    def forward(self, x1, other=1):
        v1 = self.conv1(x1)
        if (other == 1):
            other = torch.randn(v1.shape)
        v2 = self.conv2(x1)
        if (other == 1):
            other = torch.randn(v2.shape)
        return ((v1 + other) + (v2 + other))




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvifs4opu/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvifs4opu', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvifs4opu/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''