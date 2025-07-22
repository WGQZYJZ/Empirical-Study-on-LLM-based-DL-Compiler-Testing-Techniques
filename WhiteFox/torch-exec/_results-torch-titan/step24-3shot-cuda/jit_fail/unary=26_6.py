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
        self.conv_t = torch.nn.ConvTranspose2d(10, 8, 6, bias=False)
        self.conv1x1 = torch.nn.Conv2d(8, 1, 1, bias=False)
        self.conv2x2_t = torch.nn.ConvTranspose2d(1, 1, 2)

    def forward(self, x2):
        y = self.conv_t(x2)
        y = (y > 0)
        x = self.conv1x1(y)
        d = self.conv2x2_t(x)
        return d




func = Model().to('cuda')



x2 = torch.randn(1, 10, 56, 56)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Input type (CUDABoolType) and weight type (torch.cuda.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu58wnqle/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpu58wnqle', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpu58wnqle/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''