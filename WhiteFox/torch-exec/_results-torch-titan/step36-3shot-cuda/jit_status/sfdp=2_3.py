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

    def forward(self, x3, x4):
        v1 = torch.matmul(x3, x4.transpose((- 2), (- 1)))
        v2 = v1.div(1e-12)
        v3 = torch.nn.functional.dropout(v2, 0.65, False)
        v4 = v3.matmul(x4)
        return v4



func = Model().to('cuda')



x3 = torch.randn(1, 4, 8)



x4 = torch.randn(1, 5, 8)


test_inputs = [x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5_s8f0fo/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5_s8f0fo', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5_s8f0fo/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''