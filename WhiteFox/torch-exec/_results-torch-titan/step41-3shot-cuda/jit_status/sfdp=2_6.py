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

    def __init__(self, dim, dropout_p):
        super().__init__()
        self.dim = dim
        self.dropout_p = dropout_p

    def forward(self, query, key, value, training=True):
        inv_scale_factor = (1 / math.sqrt(self.dim))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p, training=training)
        output = dropout_qk.matmul(value)
        return output




dim = 10


dropout_p = 0.5

func = Model(dim, dropout_p).to('cuda')



dim = 10


query = torch.randn(2, 7, dim)



dim = 10


key = torch.randn(2, 6, dim)



dim = 10


value = torch.randn(2, 6, dim)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb2byinut/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpb2byinut', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpb2byinut/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''