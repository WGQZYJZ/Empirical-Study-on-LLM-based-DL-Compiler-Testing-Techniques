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
        self.conv_t = torch.nn.ConvTranspose2d(27, 69, 1, stride=1, padding=1, bias=False)

    def forward(self, x3):
        _paddings = torch.nn.ZeroPad2d((0, 0, 1, 1))
        x1 = _paddings(x3)
        x2 = self.conv_t(x1)
        x3 = (x2 > 0)
        x4 = (x2 * (- 12.022))
        x5 = torch.where(x3, x2, x4)
        x6 = torch.nn.functional.adaptive_avg_pool2d(torch.nn.Softplus()(x5), (1, 3))
        x7 = torch.transpose(x6, 2, 3)
        return x7




func = Model().to('cuda')



x3 = torch.randn(1, 27, 81, 61)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu2n1r5ju/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpu2n1r5ju', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpu2n1r5ju/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''