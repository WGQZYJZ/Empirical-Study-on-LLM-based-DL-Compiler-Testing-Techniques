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
        self.linear = torch.nn.Linear(2, 2)
        self.rnn = torch.nn.RNNCell(3, 2, 3)

    def forward(self, x0, x1):
        v0 = torch.nn.functional.linear(x0, self.linear.weight)
        v1 = v0.permute(0, 2, 1)
        lstm1 = torch.nn.LSTMCell(3, 2)
        lstm1(v1)
        v2 = self.rnn(v0, self.rnn.weight, self.rnn.bias)
        v3 = v2.t()
        v4 = self.rnn(v3, self.rnn.weight, self.rnn.bias)
        v5 = v4.t()
        v6 = self.rnn(v5, self.rnn.weight, self.rnn.bias)
        v7 = v6.t()
        v8 = self.rnn(v7, self.rnn.weight, self.rnn.bias)
        v9 = v8.t()
        v10 = self.rnn(v9, self.rnn.weight, self.rnn.bias)
        v11 = v10.t()
        v12 = torch.nn.functional.linear(x1, self.linear.weight)
        v13 = v12.permute(0, 2, 1)
        linear1 = torch.nn.Linear(2, 2)
        linear1(v13)
        self.rnn(v12, self.rnn.weight, self.rnn.bias)
        return v11.transpose(0, 1)



func = Model().to('cuda')


x0 = torch.randn(1, 3, 2)

x1 = torch.randn(1, 3, 2)

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
LSTMCell: Expected input to be 1D or 2D, got 3D instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe_qwt83r/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpe_qwt83r/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpe_qwt83r', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''