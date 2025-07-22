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

    def __init__(self, d_model, heads=8):
        super().__init__()
        self.scale_factor = (d_model ** (- 0.5))

    def forward(self, query, key, value, dropout_p=0.3):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        y = dropout_qk.matmul(value)
        return y



d_model = 1

func = Model(d_model).to('cuda')



query = torch.randn(1, 1, 700)



key = torch.randn(1, 1, 700)



value = torch.randn(1, 1, 700)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdq5jaalc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdq5jaalc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdq5jaalc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''