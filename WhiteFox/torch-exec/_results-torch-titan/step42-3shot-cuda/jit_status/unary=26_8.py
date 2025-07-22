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
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, 9, stride=4, padding=0, bias=False)

    def forward(self, x2):
        r1 = self.conv_t(x2)
        r2 = (r1 > 0)
        r3 = (r1 * (- 0.4))
        r4 = self.sub_850(torch.tensor([1.0], device=r1.device), r1)
        r5 = torch.where(r2, r1, r3)
        r6 = (r5 + r4)
        return r6




class SubModule_1206(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x6):
        s1 = (x6 + torch.tensor([0.0485], device=x6.device))
        s2 = (x6 + torch.tensor([0.2417], device=x6.device))
        s3 = (x6 + torch.tensor([0.1407], device=x6.device))
        s6 = (x6 * torch.tensor([0.1], device=x6.device))
        return s6




func = SubModule_1206().to('cuda')



x2 = torch.randn(72, 1, 96, 96)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdlwu7tyd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdlwu7tyd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdlwu7tyd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''