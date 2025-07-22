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
        self.conv2d1 = torch.nn.Conv2d(1, 1, 2)
        self.batch_norm1 = torch.nn.BatchNorm2d(1)
        self.conv_transpose2d1 = torch.nn.ConvTranspose2d(1, 1, 1)
        self.interpolate1 = torch.nn.Upsample(scale_factor=1)

    def forward(self, x):
        x = self.conv2d1(x)
        x = self.batch_norm1(x)
        x = self.conv_transpose2d1(x)
        y = self.interpolate1(x)
        return y




func = Model().to('cuda')



x = torch.randn(1, 1, 4, 4)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf17jkt8f/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpf17jkt8f', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpf17jkt8f/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''