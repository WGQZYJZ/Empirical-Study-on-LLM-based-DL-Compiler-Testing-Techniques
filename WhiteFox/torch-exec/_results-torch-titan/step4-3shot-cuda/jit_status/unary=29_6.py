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

    def __init__(self, min_value=(- 0.19839155912338596), max_value=7.613178804127784):
        super().__init__()
        self.convtran_1 = torch.nn.ConvTranspose2d(3, 64, 4, stride=2, padding=1)
        self.convtran_1_2 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1)
        self.convtran_1_3 = torch.nn.ConvTranspose2d(64, 3, 4, stride=2, padding=1)
        self.relu = torch.nn.ReLU(True)
        self.tanh = torch.nn.Tanh()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.convtran_1(x1)
        v2 = self.convtran_1_2(v1)
        v3 = self.convtran_1_3(v2)
        v4 = torch.clamp(v3, self.min_value, self.max_value)
        v5 = self.relu(v4)
        v6 = self.tanh(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp47crpfb2/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp47crpfb2', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp47crpfb2/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''