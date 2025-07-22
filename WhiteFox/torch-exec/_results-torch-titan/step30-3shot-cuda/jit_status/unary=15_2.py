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
        self.deconv1 = torch.nn.ConvTranspose2d(4, 3, 4, stride=2, padding=0, dilation=1)
        self.deconv2 = torch.nn.ConvTranspose2d(3, 4, 3, stride=1, padding=0, dilation=1)
        self.bn1 = torch.nn.BatchNorm2d(4)

    def forward(self, x1):
        v1 = self.deconv1(x1)
        v2 = self.bn1(self.deconv2(v1))
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzz7fm9l8/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzz7fm9l8', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzz7fm9l8/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''