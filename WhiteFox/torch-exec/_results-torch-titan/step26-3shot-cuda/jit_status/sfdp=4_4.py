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

    def __init__(self, dim, num_heads):
        super().__init__()
        self.QKV = torch.nn.Linear(dim, (dim * 3), bias=False)

    def forward(self, x1):
        qkv = self.QKV(x1)
        (q, k, v) = torch.chunk(qkv, chunks=3, dim=(- 1))
        q = (q / math.sqrt(q.size((- 1))))
        qk = (q @ k.transpose((- 1), (- 2)))
        attn_w = torch.softmax(qk, dim=(- 1))
        return (attn_w @ v)



dim = 1
num_heads = 1
func = Model(32, 4).to('cuda')



x1 = torch.randn(2, 4, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8i13tbur/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8i13tbur', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8i13tbur/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''