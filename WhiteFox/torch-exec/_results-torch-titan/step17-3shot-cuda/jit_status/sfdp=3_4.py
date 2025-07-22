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
        self.qk_mat = torch.nn.Linear(32, 32)

    def forward(self, q, k, v, mask):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scale_factor = (k.size((- 1)) ** (- 0.5))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.7)
        qk_dropout = dropout_qk.matmul(v)
        return qk_dropout



func = Model().to('cuda')



_q = torch.randn(16, 32)



_k = torch.randn(16, 32)



_v = torch.randn(16, 32)


_k = torch.randn(16, 32)


_q = torch.randn(16, 32)



_mask = torch.ones(_q.size(0), _k.size(0))


test_inputs = [_q, _k, _v, _mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8ca_8ww_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8ca_8ww_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8ca_8ww_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''