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
        self.conv_t = torch.nn.ConvTranspose2d(19, 66, 2, stride=2, padding=0)
        self.negative_slope = 10000

    def forward(self, x5):
        x6 = self.conv_t(x5)
        x7 = (x6 > 0)
        x8 = (x6 * self.negative_slope)
        x9 = torch.where(x7, x6, x8)
        return x9




func = Model().to('cuda')



x5 = torch.randn(3, 19, 4, 4)


test_inputs = [x5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6km40czt/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6km40czt', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6km40czt/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''