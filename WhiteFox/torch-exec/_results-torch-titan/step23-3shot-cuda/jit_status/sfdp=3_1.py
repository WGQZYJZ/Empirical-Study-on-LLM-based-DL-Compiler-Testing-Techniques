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

    def __init__(self, query_dim, value_dim):
        super().__init__()
        self.query_dim = query_dim
        self.value_dim = value_dim
        self.scale_factor = (query_dim ** (- 0.5))
        self.dropout = torch.nn.Dropout(p=0.3)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        dropout_qk = self.dropout(scaled_qk.softmax(dim=(- 1)))
        output = dropout_qk.matmul(value)
        return output



query_dim = 1
value_dim = 1
func = Model(10, 20).to('cuda')



query = torch.randn(2, 5, 10)



key = torch.randn(2, 100, 10)



value = torch.randn(2, 100, 20)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0rm20fsv/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0rm20fsv', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0rm20fsv/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''