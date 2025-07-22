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
        self.conv = torch.nn.Conv2d(3, 16, (2, 2), stride=(2, 2), padding=(1, 1))
        self.prelu = torch.nn.PReLU()
        self.max_pool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.act = torch.nn.ELU()
        self.bn = torch.nn.BatchNorm2d(16)

    def forward(self, x1):
        x1 = self.conv(x1)
        x2 = self.prelu(x1)
        x3 = self.max_pool(x2)
        x4 = self.act(x3)
        x5 = self.bn(x4)
        return x5




func = Model().to('cuda')



x1 = torch.randn(5, 3, 224, 224)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpurnm2se5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpurnm2se5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpurnm2se5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''