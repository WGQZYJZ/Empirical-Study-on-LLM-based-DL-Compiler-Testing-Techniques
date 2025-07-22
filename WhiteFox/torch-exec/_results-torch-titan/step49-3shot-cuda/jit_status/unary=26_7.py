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
        self.conv_t = torch.nn.ConvTranspose2d(141, 40, 4, stride=2, padding=3, bias=False)

    def forward(self, x12):
        y1 = self.conv_t(x12)
        y2 = (y1 > 0)
        y3 = (y1 * 1.244)
        y4 = torch.where(y2, y1, y3)
        return torch.nn.functional.upsample(y4, size=(174, 110), mode='bicubic')




func = Model().to('cuda')



x12 = torch.randn(16, 141, 77, 60)


test_inputs = [x12]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1joqg2eb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1joqg2eb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1joqg2eb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''