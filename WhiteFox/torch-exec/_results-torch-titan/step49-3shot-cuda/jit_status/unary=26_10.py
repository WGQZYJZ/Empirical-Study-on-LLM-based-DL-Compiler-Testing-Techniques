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
        super(Model, self).__init__()
        self.conv_t = torch.nn.ConvTranspose2d(623, 154, 6, stride=1, padding=2, bias=True)

    def forward(self, x2):
        k1 = self.conv_t(x2)
        k2 = (k1 > 0)
        k3 = (k1 * (- 0.608))
        k4 = torch.where(k2, k1, k3)
        return torch.nn.functional.adaptive_avg_pool2d(k4, (1, 1))




func = Model().to('cuda')



x2 = torch.randn(6, 623, 73, 36)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpelpz_y2y/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpelpz_y2y', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpelpz_y2y/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''