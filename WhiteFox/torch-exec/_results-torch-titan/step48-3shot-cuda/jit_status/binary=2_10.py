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
        self.conv0 = torch.nn.Conv2d(32, 32, kernel_size=(1, 3), stride=(1, 1), padding=(0, 1), dilation=(1, 1), groups=1)
        self.batchnorm0 = torch.nn.BatchNorm2d(32)

    def forward(self, x2):
        v1 = self.conv0(x2)
        v2 = self.batchnorm0(v1)
        return (v2 + (- 0.114))




func = Model().to('cuda')



x2 = torch.randn(1, 32, 24, 24)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprd74ty0e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprd74ty0e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprd74ty0e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''