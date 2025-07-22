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
        self.query = torch.nn.Linear(7, 136)
        self.key = torch.nn.Linear(7, 136)
        self.value = torch.nn.Linear(7, 136)

    def forward(self, x1):
        v1 = self.query(x1)
        v2 = self.key(x1)
        v3 = self.value(x1)
        v4 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v5 = v4.div(0.01)
        v6 = v5.softmax(dim=(- 1))
        v7 = torch.nn.functional.dropout(v6, 0.8)
        v8 = torch.matmul(v7, v3)
        return v8



func = Model().to('cuda')



x1 = torch.randn(1, 7)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmewgesaf/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpmewgesaf', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpmewgesaf/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''