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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, stride=2, padding=1))

    def forward(self, x1):
        v1 = self.features(x1)
        v2 = torch.mean(v1, dim=(2, 3), keepdims=False)
        v3 = self.features(x1)
        v4 = torch.mean(v3, dim=(2, 3), keepdims=False)
        v5 = self.features(x1)
        v6 = torch.mean(v5, dim=(2, 3), keepdims=False)
        v7 = (v4 - v6)
        v8 = F.relu(v7)
        v9 = (v2 - 0.5)
        v10 = F.relu(v9)
        v11 = (v10 + v8)
        v12 = torch.abs(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6vox4isq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6vox4isq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6vox4isq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''