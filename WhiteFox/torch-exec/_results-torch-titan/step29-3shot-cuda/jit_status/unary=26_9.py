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
        self.conv_t1 = torch.nn.ConvTranspose2d(1, 1, 3, stride=1)
        self.conv_t2 = torch.nn.ConvTranspose2d(1, 1, 3, stride=2)
        self.conv_t3 = torch.nn.ConvTranspose2d(1, 1, 3, stride=2)
        self.conv_t4 = torch.nn.ConvTranspose2d(1, 1, 3, stride=3)

    def forward(self, x0):
        t1 = self.conv_t1(x0)
        t2 = self.conv_t2(t1)
        t3 = self.conv_t3(t2)
        t4 = self.conv_t4(t3)
        return t4




func = Model().to('cuda')



x0 = torch.randn(1, 1, 8, 8)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphlm8t_ng/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmphlm8t_ng', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmphlm8t_ng/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''