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

    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, q, k, v, scale_factor=None):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        if (scale_factor is not None):
            scaled_qk = qk.mul(scale_factor)
        else:
            scaled_qk = qk
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        return dropout_qk.matmul(v)



func = Model().to('cuda')



q = torch.randn(1, 16, 64, 64)



k = torch.randn(1, 16, 64, 64)



v = torch.randn(1, 16, 64, 64)


test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp10ov55hx/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp10ov55hx', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp10ov55hx/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''