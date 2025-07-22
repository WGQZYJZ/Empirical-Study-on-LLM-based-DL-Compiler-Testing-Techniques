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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.ones_like(v1)
        v4 = (v1 + v2)
        v5 = torch.relu(v4)
        v7 = (v5 ** 4)
        v8 = self.conv2(v7)
        v9 = (v1 + x)
        v10 = torch.relu(v9)
        v11 = (v7 + v8)
        v12 = torch.relu(v11)
        v13 = self.conv3(v12)
        v14 = torch.ones_like(v13)
        v16 = (v13 + v14)
        v17 = torch.relu(v16)
        return v17




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpoc8dzbkz/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpoc8dzbkz', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpoc8dzbkz/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''