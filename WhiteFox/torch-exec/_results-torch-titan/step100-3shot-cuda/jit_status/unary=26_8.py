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
        self.conv_t = torch.nn.ConvTranspose2d(17, 36, 21, stride=1, padding=0, bias=False)

    def forward(self, x0):
        v1 = self.conv_t(x0)
        v2 = v1
        v3 = (v1 > (- 4.54))
        v4 = torch.where(v3, v2, torch.tensor(True))
        return v4




func = Model().to('cuda')



x0 = torch.randn(3, 17, 14, 12)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppfe02sz1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppfe02sz1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppfe02sz1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''