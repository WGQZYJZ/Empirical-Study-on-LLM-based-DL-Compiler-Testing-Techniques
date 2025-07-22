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
        self.module_0 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())
        self.module_1 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())
        self.module_2 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())
        self.module_3 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())
        self.module_4 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())
        self.module_5 = torch.nn.Sequential(torch.nn.ReLU(), torch.nn.ConvTranspose2d(3, 3, [3, 4], stride=[1, 2], padding=(1, 3)), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.module_0(x1)
        v2 = self.module_1(v1)
        v3 = self.module_2(v2)
        v4 = self.module_3(v3)
        v5 = self.module_4(v4)
        v6 = self.module_5(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyo1abla4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpyo1abla4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpyo1abla4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''