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
        self.key = nn.Linear(512, 512, bias=False)
        self.query = nn.Linear(512, 512, bias=False)
        self.value = nn.Linear(512, 512, bias=False)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, inputs):
        key = self.key(inputs)
        query = self.query(inputs)
        value = self.value(inputs)
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(5)
        softmax_qk = self.softmax(scaled_qk)
        return self.dropout(softmax_qk).matmul(value).transpose((- 2), (- 1))



func = Model().to('cuda')



_inputs__ = torch.randn(8, 16, 512)


test_inputs = [_inputs__]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmph3fm4347/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmph3fm4347', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmph3fm4347/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''