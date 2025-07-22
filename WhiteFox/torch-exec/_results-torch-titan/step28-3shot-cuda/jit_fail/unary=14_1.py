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

    def forward(self, x1):
        v1 = torch.nn.ConvTranspose2d(64, 64, (2, 2), stride=(2, 2), padding=(0, 0))(x1)
        v2 = torch.nn.Sigmoid()(v1)
        v3 = (v2 * v1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 64, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpomlxm_t_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpomlxm_t_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpomlxm_t_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''