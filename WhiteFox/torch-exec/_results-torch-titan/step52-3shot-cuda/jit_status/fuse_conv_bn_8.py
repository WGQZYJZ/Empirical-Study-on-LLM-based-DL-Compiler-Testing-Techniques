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
        self.bn1 = torch.nn.BatchNorm1d(6)
        self.bn2 = torch.nn.BatchNorm1d(6)
        self.bn3 = torch.nn.BatchNorm1d(6)
        self.bn4 = torch.nn.BatchNorm1d(6)

    def forward(self, x3):
        s1 = self.bn1(x3)
        s2 = self.bn2(s1)
        s3 = self.bn3(s2)
        s4 = self.bn4(s3)
        return s4[0]




func = Model().to('cuda')



x3 = torch.randn(3, 6, requires_grad=False)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp36dktof9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp36dktof9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp36dktof9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''