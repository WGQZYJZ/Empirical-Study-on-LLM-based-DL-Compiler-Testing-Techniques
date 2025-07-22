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
        self.conv_transpose = torch.nn.ConvTranspose2d(7, 20, 1, stride=1, padding=0)

    def forward(self, x0):
        v0 = self.conv_transpose(x0)
        v1 = (v0 * 0.21449275362394013)
        v2 = (v0 * 0.4933822846162827)
        v3 = (v0 * 0.5077301052518364)
        v4 = torch.erf(v0)
        v5 = (v4 + 1)
        v6 = (v3 * v5)
        return v6




func = Model().to('cuda')



x0 = torch.randn(8, 7, 35, 35)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqk6ao9xp/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqk6ao9xp', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqk6ao9xp/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''