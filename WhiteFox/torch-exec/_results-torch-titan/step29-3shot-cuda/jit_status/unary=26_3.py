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
        self.conv_t1 = torch.nn.ConvTranspose2d(10, 20, 3, stride=2, padding=1, output_padding=1)
        self.conv_t2 = torch.nn.ConvTranspose2d(20, 30, 3, stride=2, padding=1, output_padding=1)
        self.conv_t3 = torch.nn.ConvTranspose2d(30, 10, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x4):
        t1 = self.conv_t1(x4)
        t2 = self.conv_t2(t1)
        t3 = self.conv_t3(t2)
        return t3




func = Model().to('cuda')



x4 = torch.randn(6, 10, 8, 8)


test_inputs = [x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpupczl4lo/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpupczl4lo', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpupczl4lo/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''