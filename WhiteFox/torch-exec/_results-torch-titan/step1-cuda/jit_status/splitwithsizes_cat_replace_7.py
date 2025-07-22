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
        self.split = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 3)

    def forward(self, x):
        v1 = self.split(x)
        v2 = [v1, v1, v1]
        v3 = torch.cat(v2, 1)
        v4 = v3.shape
        v5 = v4[2]
        v6 = v4[3]
        v7 = v3[:, :, :, 0:1]
        v8 = v3[:, :, :, 1:2]
        v9 = v3[:, :, :, 2:3]
        v10 = (v7 + 0.9)
        v11 = (v8 + 0.8)
        v12 = (v9 + 0.7)
        v13 = (v10 + 0.6)
        v14 = (v11 - 0.5)
        v15 = (v12 * 0.8)
        v16 = (v13 * 0.7)
        v17 = (v15 * 0.6)
        v18 = (v16 + 0.5)
        return ((v14 + v17) + v18)



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdt70wefj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdt70wefj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdt70wefj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''