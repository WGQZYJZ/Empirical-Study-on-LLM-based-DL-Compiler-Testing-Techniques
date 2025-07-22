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
        self.query_conv = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.key_conv = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.scale_factor = (1 / math.sqrt(64))
        self.dropout_p = 0.5

    def forward(self, x1):
        q = self.query_conv(x1)
        k = self.key_conv(x1)
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        v = torch.randn_like(k)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



x1 = torch.randn(4, 64, 24, 24)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7w2bpex8/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7w2bpex8', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7w2bpex8/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''