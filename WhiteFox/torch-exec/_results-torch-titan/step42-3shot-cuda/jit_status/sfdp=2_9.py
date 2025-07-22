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



class Model(torch.nn.modules.Module):

    def __init__(self, dim, dropout_p, inv_scale_factor):
        super().__init__()
        self.scale_factor = (dim ** (- 0.5))
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        dropped_qk = torch.nn.functional.dropout(scaled_qk, p=self.dropout_p)
        output = dropped_qk.matmul(value)
        return output



dim = 1
dropout_p = 1
inv_scale_factor = 1

func = Model(dim, dropout_p, inv_scale_factor).to('cuda')



query = torch.randn(33, 128)



key = torch.randn(32, 128)



value = torch.randn(32, 128)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpoji1fnin/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpoji1fnin', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpoji1fnin/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''