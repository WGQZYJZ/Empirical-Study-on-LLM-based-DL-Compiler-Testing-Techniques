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

    def forward(self, x1):
        t1 = torch.full([976, 1024], -0.00051707, dtype=torch.float16, layout=torch.strided, device=torch.device('cuda:0'), pin_memory=False)
        t2 = torch.exp(t1)
        t3 = t2 * torch.sqrt(torch.tensor(795.94091796875)).to(dtype=torch.float16)
        t4 = torch.rand(976, 1024, dtype=torch.float16, layout=torch.strided, device=torch.device('cuda:0'), pin_memory=False)
        t5 = t4 * t3
        t6 = t5 * -0.03736045416835785
        t7 = t6 + 0.013442041213035582
        t8 = torch.sigmoid(t7)
        t9 = t8 * 0.05528832020091057
        t10 = t9 + 0.003260288772518639
        t11 = t10 - 0.013401031310820584
        t12 = t11 * -0.008240049831323624
        t13 = t12 + 0.018585406033706665
        t14 = torch.ceil(t13)
        t15 = t14 - 1.0
        t16 = torch.mul(t15, -0.010231505373716355)
        t17 = t16 + 0.02776596259784794
        t18 = torch.mul(t17, -0.01909807580719948)
        t19 = t18 - 0.009946531035437583
        t20 = t19 - 0.8235650873184204
        t21 = torch.mul(t20, 2.064790058135986)
        t22 = t21 + 1.5
        return t22



func = Model().to('cpu')


x1 = torch.randn(976, 1024, device='cuda:0')

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpexgt9cin/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpexgt9cin/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpexgt9cin', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''