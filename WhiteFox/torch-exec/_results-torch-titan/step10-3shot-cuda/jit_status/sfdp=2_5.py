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

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = query.bmm(key.transpose(1, 2))
        scaled_qk = (qk / inv_scale_factor.view(qk.shape[0], qk.shape[1], 1)).softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        output = dropout_qk.bmm(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 12, 512)



key = torch.randn(1, 12, 512)



value = torch.randn(1, 12, 512)



inv_scale_factor = torch.randn(12)

dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe142y_r3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpe142y_r3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpe142y_r3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''