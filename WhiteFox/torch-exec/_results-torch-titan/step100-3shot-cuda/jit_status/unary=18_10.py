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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=(2, 1), padding=(2, 1))
        self.conv2 = torch.nn.Conv2d(16, 16, 5, stride=(2, 1), padding=(1, 2))
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=(1, 1), padding=0)

    def forward(self, x3):
        v1 = torch.sigmoid(self.conv1(x3))
        v2 = torch.sigmoid(self.conv2(v1))
        v3 = self.conv3(v2)
        return v3




func = Model().to('cuda')



x3 = torch.randn(53, 16, 50, 66)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8jff45iq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8jff45iq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8jff45iq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''