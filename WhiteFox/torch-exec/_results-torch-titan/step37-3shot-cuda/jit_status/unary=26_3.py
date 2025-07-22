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
        self.conv_t = torch.nn.ConvTranspose2d(248, 3, 3, stride=2, padding=2, output_padding=1)

    def forward(self, x2):
        n1 = self.conv_t(x2)
        n2 = (n1 > 0)
        n3 = (n1 * (- 0.5))
        n4 = torch.where(n2, n1, n3)
        return torch.nn.functional.adaptive_avg_pool2d(torch.nn.functional.hardtanh(n4, (- 8), 8), (1, 1))




func = Model().to('cuda')



x2 = torch.randn(89, 248, 7, 25)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1tfypiji/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1tfypiji', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1tfypiji/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''