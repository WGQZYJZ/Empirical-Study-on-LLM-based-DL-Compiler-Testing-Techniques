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
        self.dropout_p = 0
        self.query = torch.nn.Parameter(torch.rand((128, 64)))
        self.key = torch.nn.Parameter(torch.rand((256, 64)))
        self.value = torch.nn.Parameter(torch.rand((256, 64)))

    def forward(self, input1):
        q = self.query.unsqueeze(0)
        k = self.key
        v = self.value
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk / math.sqrt(v.size((- 1))))
        softmax_qk = torch.softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')

input1 = 1

test_inputs = [input1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgxu3vfmm/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgxu3vfmm', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgxu3vfmm/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''