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
        v1 = x1.view((- 1))
        v2 = v1.size(0)
        v3 = torch.zeros(v2, dtype=torch.float32, device=torch.device('cuda:0'))
        v4 = torch.sigmoid(v3)
        v5 = (v1 * v4)
        x2 = v5.view(1, (- 1))
        return x2



func = Model().to('cuda')




x1 = torch.rand(1, 200, dtype=torch.float32).cuda()


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpuqtvz1u_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpuqtvz1u_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpuqtvz1u_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''