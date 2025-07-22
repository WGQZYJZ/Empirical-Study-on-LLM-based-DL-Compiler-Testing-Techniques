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

    def __init__(self, d_model):
        super().__init__()
        self.d_model = d_model

    def forward(self, k, v, q, scale_factor, dropout_p):
        scale = (1 / scale_factor)
        a = torch.matmul(q, k.transpose((- 2), (- 1)))
        a = (a * scale)
        b = F.softmax(a, dim=(- 1))
        c = F.dropout(b, p=dropout_p, training=self.training)
        d = torch.matmul(c, v)
        return d




d_model = 64

func = Model(d_model).to('cuda')



d_model = 64


k = torch.randn(d_model, 1, 32)



d_model = 64


v = torch.randn(d_model, 1, 32)



d_model = 64


q = torch.randn(d_model, 1, 32)

scale_factor = 1
dropout_p = 1

test_inputs = [k, v, q, scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzagt6o3w/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzagt6o3w', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzagt6o3w/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''