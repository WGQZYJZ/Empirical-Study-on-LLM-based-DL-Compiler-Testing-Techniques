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
        self.query = torch.nn.Linear(64, 32)
        self.key = torch.nn.Linear(64, 32)
        self.scale_factor = torch.sqrt(torch.FloatTensor([64.0]))
        self.dropout = torch.nn.Dropout(0.33)

    def forward(self, x1):
        v1 = self.query(x1)
        v2 = self.dropout(self.key(x1))
        v3 = torch.matmul(v1, v2.transpose((- 1), (- 2)))
        v4 = v3.div(self.scale_factor)
        v5 = F.softmax(v4, dim=(- 1))
        v6 = self.dropout(v5)
        v7 = torch.matmul(v6, x1)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6z_s1hw1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6z_s1hw1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6z_s1hw1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''