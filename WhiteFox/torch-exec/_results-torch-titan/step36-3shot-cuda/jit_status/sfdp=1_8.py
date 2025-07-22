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

    def forward(self, q1, k1, v1, inv_scale_factor, dropout_p, dropout_m, dropout_inplace):
        qk = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        if (dropout_m is None):
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p, inplace=dropout_inplace)
        else:
            dropout_qk_mask = torch.nn.functional.dropout(torch.ones_like(softmax_qk), p=dropout_p, inplace=dropout_inplace)
            dropout_qk = softmax_qk.mul(dropout_qk_mask).div((1.0 - dropout_m))
        return dropout_qk.matmul(v1)



func = Model().to('cuda')



q1 = torch.randn(1, 8, 5)



k1 = torch.randn(1, 6, 5)



v1 = torch.randn(1, 6, 5)



inv_scale_factor = torch.tensor(1e-05)

dropout_p = 1
dropout_m = 1
dropout_inplace = 1

test_inputs = [q1, k1, v1, inv_scale_factor, dropout_p, dropout_m, dropout_inplace]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp10getpfj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp10getpfj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp10getpfj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''