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



class m1(nn.Module):

    def __init__(self):
        super().__init__()
        self.p1 = torch.rand(1)
        self.p2 = torch.nn.Parameter(torch.randn(1))

    def forward(self, x1):
        x2 = torch.nn.functional.relu(((self.p1 * x1) + self.p2))
        return x2




func = m1().to('cuda')



x1 = torch.randn(3, 4)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptvn2luhi/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmptvn2luhi', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmptvn2luhi/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''