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
        self.dropout_p = 0.5
        self.scale_factor = np.sqrt(32 / (0.0212 * 8))

    def forward(self, x1, x2):
        q1 = torch.nn.functional.linear(x1, x2)
        k1 = torch.nn.functional.linear(x1, x2)
        v1 = torch.nn.functional.tanh(torch.nn.functional.linear(x1, x2))
        qk1 = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk1 = qk1.mul(self.scale_factor)
        dropout_qk1 = torch.nn.functional.dropout(scaled_qk1.softmax(dim=-1), p=self.dropout_p)
        output1 = dropout_qk1.matmul(v1)
        return output1


func = Model().to('cuda')


x1 = torch.randn(1, 32)

x2 = torch.randn(32, 32)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvr20__5a/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpvr20__5a/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpvr20__5a', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''