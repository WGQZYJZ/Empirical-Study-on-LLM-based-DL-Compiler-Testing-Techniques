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
        self.query = torch.nn.Linear(64, 64)
        self.key = torch.nn.Linear(64, 64)
        self.value = torch.nn.Linear(64, 64)
        self.attn_mask = torch.nn.Parameter(torch.tril(torch.ones(1, 96, 96)))

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        qk = ((q @ k.transpose((- 2), (- 1))) / math.sqrt(q.size((- 1))))
        qk = (qk + self.attn_mask)
        weight = torch.softmax(qk, dim=(- 1))
        output = (weight @ v)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 96, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpj5s2qtw9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpj5s2qtw9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpj5s2qtw9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''