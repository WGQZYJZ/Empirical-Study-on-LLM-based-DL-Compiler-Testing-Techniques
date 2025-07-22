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

    def __init__(self, dropout_p, scale_factor):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, x1, x2, x3):
        q1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        q2 = q1.div(self.scale_factor)
        q3 = q2.softmax(dim=(- 1))
        q4 = torch.nn.functional.dropout(q3, p=self.dropout_p)
        q5 = torch.matmul(q4, x3)
        return q5



dropout_p = 1
scale_factor = 1

func = Model(dropout_p, scale_factor).to('cuda')



x1 = torch.randn(1, 64, 32, 32)



x2 = torch.randn(1, 64, 32, 32)



x3 = torch.randn(1, 64, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpy13xrl2l/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpy13xrl2l', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpy13xrl2l/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''