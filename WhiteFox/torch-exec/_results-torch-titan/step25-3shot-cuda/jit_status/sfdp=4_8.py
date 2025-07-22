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

    def forward(self, q, k, v, attn_mask):
        attn_weight = F.softmax((q @ k.transpose((- 2), (- 1))), dim=(- 1))
        attn_weight *= attn_mask
        output = (attn_weight @ v)
        output *= attn_mask
        return (q, k, v, attn_mask, attn_weight, output)



func = Model().to('cuda')



q = torch.randn(1, 3, 64, 64)



k = torch.randn(1, 3, 64, 64)



v = torch.randn(1, 3, 64, 64)



attn_mask = torch.ones(1, 3, 64, 64).bool()


test_inputs = [q, k, v, attn_mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppwbktt51/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppwbktt51', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppwbktt51/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''