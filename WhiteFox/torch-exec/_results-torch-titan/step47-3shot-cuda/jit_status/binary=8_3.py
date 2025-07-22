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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3, x4, x5):
        a1 = self.conv1(x1)
        a2 = self.conv1(x2)
        a3 = self.conv1(x3)
        a4 = self.conv1(x4)
        a5 = self.conv1(x5)
        a6 = ((((a1 * a2) * a3) * a4) * a5)
        a7 = a2.mul_(a1)
        a8 = a6.mul(a7)
        a9 = a1.mul(a2).mul(a3).mul(a4).mul(a5)
        return a8.div(a9)




func = Model().to('cuda')



x1 = torch.randn(4, 3, 64, 64)



x2 = torch.randn(4, 3, 64, 64)



x3 = torch.randn(4, 3, 64, 64)



x4 = torch.randn(4, 3, 64, 64)



x5 = torch.randn(4, 3, 64, 64)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxmv0imvq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpxmv0imvq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpxmv0imvq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''