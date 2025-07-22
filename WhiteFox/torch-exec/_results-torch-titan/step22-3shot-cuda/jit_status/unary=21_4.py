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

    def __init__(self):
        super().__init__()
        self.conv_0 = torch.nn.Conv2d(3, 32, kernel_size=(1, 3), stride=(1, 2))
        self.n25 = torch.nn.ReLU()
        self.conv_1 = torch.nn.Conv2d(32, 32, kernel_size=(2, 3), stride=(2, 2))

    def forward(self, x):
        v0 = torch.tanh(self.conv_0(x))
        v1 = self.n25(v0)
        v2 = torch.tanh(self.conv_1(v1))
        return v2




func = ModelTanh().to('cuda')



x0 = torch.randn(20, 3, 128, 67)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjv61hh_q/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpjv61hh_q', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpjv61hh_q/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''