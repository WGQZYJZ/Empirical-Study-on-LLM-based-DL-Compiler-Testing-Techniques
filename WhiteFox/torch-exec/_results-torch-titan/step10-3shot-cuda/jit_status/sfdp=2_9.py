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

    def forward(self, query, key, value, inv_scale_factor1):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk * inv_scale_factor1)
        softmax_qk = torch.nn.functional.dropout(F.softmax(scaled_qk, dim=(- 1)), p=0.2)
        output = torch.matmul(softmax_qk, value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 1, 3, 5)



key = torch.randn(1, 1, 2, 5)



value = torch.randn(1, 1, 2, 5)



inv_scale_factor1 = torch.randn(1)


test_inputs = [query, key, value, inv_scale_factor1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8z_266ia/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8z_266ia', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8z_266ia/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''