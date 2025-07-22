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
        self.conv_t = torch.nn.ConvTranspose2d(3, 4, 3, stride=2, padding=1, bias=False)

    def forward(self, x4):
        w = torch.randn(2, 3, 3, 3)
        z = torch.nn.functional.conv2d(x4, w, bias=None, stride=2, padding=0)
        z1 = self.conv_t(x4)
        return torch.nn.functional.interpolate(z1, scale_factor=[1.0, 1.0])




func = Model().to('cuda')



x4 = torch.randn(3, 3, 15, 15)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpm1vls_ta/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpm1vls_ta', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpm1vls_ta/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''