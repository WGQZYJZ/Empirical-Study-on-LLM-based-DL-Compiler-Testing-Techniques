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

    def forward(self, q1, k1, v1, scale_factor, dropout_p):
        qk = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)
        return output



func = Model().to('cuda')



q1 = torch.randn(1, 3, 64, 64)



k1 = torch.randn(1, 3, 64, 64)



v1 = torch.randn(1, 16, 64, 64)



scale_factor = torch.tensor(1)



dropout_p = torch.tensor(0.5)


test_inputs = [q1, k1, v1, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (16) at non-singleton dimension 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8nw087u_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8nw087u_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8nw087u_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''