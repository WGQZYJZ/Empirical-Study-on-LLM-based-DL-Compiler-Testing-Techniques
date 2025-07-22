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

    def __init__(self, query_dim: int, key_dim: int, value_dim: int):
        super().__init__()
        self.scale_factor = (key_dim ** (- 0.5))
        self.dropout_p = 0.1

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output




query_dim = 16


key_dim = 16


value_dim = 16

func = Model(query_dim, key_dim, value_dim).to('cuda')



query_dim = 16


query = torch.randn(1, 5, query_dim)



key_dim = 16


key = torch.zeros(1, 4, key_dim)



value_dim = 16


value = torch.zeros(1, 4, value_dim)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpw9fgvt9s/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpw9fgvt9s', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpw9fgvt9s/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''