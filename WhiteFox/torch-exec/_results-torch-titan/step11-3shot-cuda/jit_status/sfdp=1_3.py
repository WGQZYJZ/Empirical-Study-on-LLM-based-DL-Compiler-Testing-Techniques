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

    def __init__(self, query_dim, key_dim, value_dim, feature_dim, num_heads, inv_scale_factor, dropout_p):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(num_heads, (query_dim // num_heads), 1, 1))
        self.key = torch.nn.Parameter(torch.randn(num_heads, (key_dim // num_heads), 1, 1))
        self.value = torch.nn.Parameter(torch.randn(num_heads, (value_dim // num_heads), 1, 1))
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax((- 1))
        self.inv_scale_factor = inv_scale_factor
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output




query_dim = 256


key_dim = 256


value_dim = 512


feature_dim = 512


num_heads = 8


inv_scale_factor = (2.0 ** 0.5)


dropout_p = 0.2

func = Model(query_dim, key_dim, value_dim, feature_dim, num_heads, inv_scale_factor, dropout_p).to('cuda')



feature_dim = 512


query = torch.randn(1, feature_dim, 1, 1)



feature_dim = 512


key = torch.randn(1, feature_dim, 1, 1)



feature_dim = 512


value = torch.randn(1, feature_dim, 1, 1)


test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6mlg6uvs/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6mlg6uvs', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6mlg6uvs/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''