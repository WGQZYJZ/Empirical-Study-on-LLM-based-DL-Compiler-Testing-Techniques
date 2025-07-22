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

    def forward(self, x1, x2):
        x3 = [x1, x2]
        x4 = torch.cat(x3, dim=1)
        x5 = x4[:, 0:9223372036854775807]
        x6 = x5[:, 0:size]
        x7 = torch.cat([x4, x6], dim=1)
        return x7



func = Model().to('cuda')



shape = (1, 3, 14, 14)


x1 = torch.randn(shape)



shape = (1, 3, 14, 14)


x2 = torch.randn(shape)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjdjjrp8n/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpjdjjrp8n', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpjdjjrp8n/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''