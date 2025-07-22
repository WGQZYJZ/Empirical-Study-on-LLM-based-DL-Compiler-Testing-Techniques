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
        self.q = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)
        self.k = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)
        self.v = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)
        self.a = torch.nn.Conv2d(3, 32, 1, stride=1, padding=0)

    def forward(self, x1, x2):
        q = self.q(x1)
        k = self.k(x2)
        v = self.v(x2)
        a = self.a(x2)
        b = (k.transpose((- 2), (- 1)) / q.size((- 1)))
        v = (torch.softmax(((q @ b) + a), dim=(- 1)) @ v)
        return v



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl8lo3lnq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl8lo3lnq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl8lo3lnq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''