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
        self.conv = torch.nn.Conv2d(1, 180, 3, stride=1, padding=4, bias=False)
        self.conv_t = torch.nn.ConvTranspose2d(180, 144, 6, stride=1, padding=4, bias=False)

    def forward(self, x2):
        h1 = torch.nn.functional.interpolate(x2, scale_factor=[0.373, 1.0])
        h2 = self.conv(h1)
        h3 = (h2 > 0)
        h4 = (h2 * (- 0.898))
        h5 = torch.where(h3, h2, h4)
        h6 = self.conv_t(h5)
        return torch.nn.functional.interpolate(torch.nn.Softplus()(h6), scale_factor=[1.0, 2.0])




func = Model().to('cuda')



x2 = torch.randn(1, 1, 71, 9)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpch3vt3ad/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpch3vt3ad', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpch3vt3ad/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''