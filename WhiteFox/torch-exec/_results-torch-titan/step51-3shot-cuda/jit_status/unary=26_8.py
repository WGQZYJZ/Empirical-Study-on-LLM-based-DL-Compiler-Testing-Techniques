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
        self.conv_t = torch.nn.ConvTranspose2d(7, 1, 9, stride=1, padding=0, bias=False)

    def forward(self, x3):
        x1 = self.conv_t(x3)
        u2 = (x1 > 0)
        u3 = (x1 * (- 0.208927))
        u4 = torch.where(u2, x1, u3)
        x5 = torch.neg(u4)
        x6 = torch.nn.functional.relu6(x5)
        return x6




func = Model().to('cuda')



x3 = torch.randn(2, 7, 14, 15)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpw6bwo9ug/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpw6bwo9ug', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpw6bwo9ug/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''