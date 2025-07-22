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
        self.conv_t = torch.nn.ConvTranspose2d(253, 79, 1, stride=1, padding=1, bias=False)

    def forward(self, x10):
        x11 = self.conv_t(x10)
        x12 = (x11 > 0)
        x13 = (x11 * 0.148)
        x14 = torch.where(x12, x11, x13)
        x15 = torch.nn.functional.adaptive_avg_pool2d(x14, (1, 1))
        x16 = torch.nn.functional.interpolate(x15, (24, 55), mode='nearest', align_corners=None)
        x17 = torch.nn.functional.interpolate(torch.nn.ReLU()(x16), size=(6, 40))
        return x17




func = Model().to('cuda')



x10 = torch.randn(1, 253, 93, 45)


test_inputs = [x10]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptouglqx4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmptouglqx4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmptouglqx4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''