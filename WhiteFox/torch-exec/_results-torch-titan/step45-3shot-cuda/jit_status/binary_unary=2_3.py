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
        self.conv1 = torch.nn.Conv2d(16, 32, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 32, 16, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(32, 64, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(64, 128, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 100)
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = (v4 - 200)
        v6 = F.relu(v5)
        v7 = self.conv3(v6)
        v8 = (v7 - 300)
        v9 = F.relu(v8)
        v10 = self.conv4(v9)
        v11 = (v10 - 400)
        v12 = F.relu(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 16, 56, 56)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8cr8qdi_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8cr8qdi_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8cr8qdi_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''