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

    def forward(self, k, q, v, scale_factor, dropout_p):
        z = torch.matmul(q, k.transpose((- 2), (- 1)))
        z = (z * scale_factor)
        m = nn.Softmax(dim=(- 1))
        m = m(z)
        m = torch.nn.functional.dropout(m, p=dropout_p)
        z = m.matmul(v)
        return z



func = Model().to('cuda')



k = torch.randn(5, 5)



q = torch.randn(5, 5)



v = torch.randn(5, 10)

scale_factor = 1
dropout_p = 1

test_inputs = [k, q, v, scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplmr9mm00/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplmr9mm00', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplmr9mm00/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''