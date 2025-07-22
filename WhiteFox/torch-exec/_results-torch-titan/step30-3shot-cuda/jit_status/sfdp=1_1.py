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

    def __init__(self, dim, num_heads, drop_p=0.1):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim, bias=True)
        self.key = torch.nn.Linear(dim, dim, bias=True)
        self.value = torch.nn.Linear(dim, dim, bias=True)
        self.scale_factor = ((dim / num_heads) ** (- 0.5))
        self.dropout_p = drop_p

    def forward(self, query, key, value):
        query = self.query(query)
        key = self.key(key)
        value = self.value(value)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output




dim = 512


num_heads = 2

func = Model(dim, num_heads, drop_p=0.1).to('cuda')



dim = 512


query = torch.randn(1, dim)



dim = 512


key = torch.randn(1, dim)



dim = 512


value = torch.randn(1, dim)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9cg855_m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9cg855_m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9cg855_m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''