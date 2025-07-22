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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(343, 257, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x4):
        q1 = self.conv_t(x4)
        q2 = (q1 > 0)
        q3 = (q1 * self.negative_slope)
        q4 = torch.where(q2, q1, q3)
        return q4




negative_slope = (- 0.01)


func = Model(negative_slope).to('cuda')



x4 = torch.randn(125, 343, 4, 4)


test_inputs = [x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpentgmwy1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpentgmwy1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpentgmwy1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''