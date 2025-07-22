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
        self.conv_t = torch.nn.ConvTranspose2d(369, 223, 5, stride=2, padding=2, bias=True)

    def forward(self, x11):
        o1 = self.conv_t(x11)
        o2 = (o1 > 0)
        o3 = (o1 * (- 0.419))
        o4 = torch.where(o2, o1, o3)
        return torch.nn.functional.adaptive_avg_pool2d(o4, (1, 1))




func = Model().to('cuda')



x11 = torch.randn(25, 369, 46, 60)


test_inputs = [x11]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1adykvaf/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1adykvaf', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1adykvaf/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''