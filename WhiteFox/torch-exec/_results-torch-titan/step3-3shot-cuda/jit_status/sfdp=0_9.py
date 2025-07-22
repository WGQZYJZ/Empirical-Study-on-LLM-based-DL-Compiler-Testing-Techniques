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



class ScaledDotProductAttention(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale):
        query = query.squeeze(1)
        key = key.squeeze(1)
        value = value.squeeze(1)
        scaled_dot_product = (torch.matmul(query, key.transpose((- 2), (- 1))) / inv_scale)
        attention_weights = scaled_dot_product.softmax(dim=(- 1))
        return attention_weights.matmul(value)



func = ScaledDotProductAttention().to('cuda')



query = torch.randn(1, 1, 256)



key = torch.randn(1, 1, 256)



value = torch.randn(1, 1, 256)

inv_scale = 1

test_inputs = [query, key, value, inv_scale]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplh4_ys4f/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplh4_ys4f', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplh4_ys4f/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''