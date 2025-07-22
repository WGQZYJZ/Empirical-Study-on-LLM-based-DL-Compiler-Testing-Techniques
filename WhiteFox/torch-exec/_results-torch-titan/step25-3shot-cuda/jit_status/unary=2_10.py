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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(nn.Conv2d(1, 6, kernel_size=5, padding=0), nn.Tanh(), nn.BatchNorm2d(6))
        self.block2 = nn.Sequential(nn.Conv2d(6, 16, kernel_size=5, padding=2), nn.Tanh(), nn.BatchNorm2d(16))
        self.transf_block = nn.ConvTranspose2d(16, 8, kernel_size=5, stride=1, padding=0, output_padding=0)

    def forward(self, x1):
        x1 = self.block1(x1)
        x1 = self.block2(x1)
        x1 = self.transf_block(x1)
        x1 = F.pad(x1, [0, 0, 0, 0, 1, 1])
        return x1




func = Model().to('cuda')



x1 = torch.randn(1, 1, 48, 48)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkz7wcmon/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpkz7wcmon', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpkz7wcmon/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''