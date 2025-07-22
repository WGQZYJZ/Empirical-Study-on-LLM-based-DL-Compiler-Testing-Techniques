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



class ModelTanh(torch.nn.Module):

    def __init__(self, in_channels, conv_dim, out_channels):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose1d(in_channels, out_channels, 3, stride=conv_dim)

    def forward(self, x):
        y = self.conv1(x)
        z = torch.tanh(y)
        return z



in_channels = 1
conv_dim = 1
out_channels = 1

func = ModelTanh(in_channels, conv_dim, out_channels).to('cuda')



x = torch.empty(3, 3, 3).uniform_()


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 3], expected input[3, 3, 3] to have 1 channels, but got 3 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmjzpyv7i/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpmjzpyv7i', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpmjzpyv7i/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''