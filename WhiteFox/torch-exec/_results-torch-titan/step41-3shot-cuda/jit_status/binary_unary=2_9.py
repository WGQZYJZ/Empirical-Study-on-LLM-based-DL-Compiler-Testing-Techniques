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
        self.conv = torch.nn.Conv2d(1, 3, 3, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 - 0.5)
        t0 = torch.tensor([[[[(- 0.4566)]], [[(- 0.4566)]], [[(- 0.4566)]]]]).to('cuda')
        v3 = (t0 + v1)
        return F.softmax(v3)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 8, 8).to('cuda')


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdff7h3ny/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdff7h3ny', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdff7h3ny/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''