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



class ModelNew2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, 2)
        self.batchnorm = torch.nn.BatchNorm2d(2)

    def forward(self, x0_1):
        x1_1 = self.conv(x0_1)
        x2_1 = self.batchnorm(x1_1)
        x3_1 = torch.rand_like(x1_1)
        x4_1 = torch.nn.functional.dropout(x3_1)
        x5_1 = torch.nn.functional.dropout(x4_1)
        x6_1 = torch.nn.functional.dropout(x5_1)
        return x6_1




func = ModelNew2().to('cuda')



x0_1 = torch.randn(2, 2, 2, 2)


test_inputs = [x0_1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2r4_rj6b/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2r4_rj6b', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2r4_rj6b/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''