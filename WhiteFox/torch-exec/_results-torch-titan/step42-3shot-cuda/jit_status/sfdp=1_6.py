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



class ScaledDotProductAttention(torch.nn.Module):

    def __init__(self, scale_factor):
        super().__init__()
        self.scale_factor = scale_factor

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        return torch.matmul(scaled_qk.softmax(dim=(- 1)), value)



scale_factor = 1
func = ScaledDotProductAttention(math.sqrt(0.5)).to('cuda')



query = torch.randn(1, 16, 64)



key = torch.randn(1, 16, 64)



value = torch.randn(1, 16, 64)

dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpklz36nro/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpklz36nro', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpklz36nro/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''