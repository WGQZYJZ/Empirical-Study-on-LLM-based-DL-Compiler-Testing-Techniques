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
        self.conv = torch.nn.Conv2d(91, 2, 3, stride=2, padding=1)
        self.bn = torch.nn.BatchNorm2d(2)
        self.fc = torch.nn.Linear(2, 1284)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        v12 = self.fc(v11)
        v13 = (v12 * 0.5)
        v14 = (v12 * v12)
        v15 = (v14 * v12)
        v16 = (v15 * 0.044715)
        v17 = (v12 + v16)
        v18 = (v17 * 0.7978845608028654)
        v19 = torch.tanh(v18)
        v20 = (v19 + 1)
        v21 = (v13 * v20)
        return v21




func = Model().to('cuda')



x1 = torch.randn(1, 91, 256, 4)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpama79onu/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpama79onu', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpama79onu/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''