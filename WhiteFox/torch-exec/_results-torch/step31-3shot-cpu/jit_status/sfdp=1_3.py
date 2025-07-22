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
        self.mat = torch.nn.Linear(3, 3)
        self.dropout = torch.nn.Dropout(0.8)

    def forward(self, x1, x2, x3, x4):
        q = self.mat(x1)
        k = self.mat(x2)
        k = k.T
        v = self.mat(x3)
        qk = torch.matmul(q, k)
        inv_scale_factor = torch.sqrt(torch.as_tensor(q.size(-1)).float()).reciprocal()
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        drop_qk = self.dropout(softmax_qk)
        o = torch.matmul(drop_qk, v)
        return (o, o)


func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

x3 = torch.randn(3, 3)

x4 = torch.randn(3, 3)

test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqkcx4q78/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpqkcx4q78/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpqkcx4q78', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''