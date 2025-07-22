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
        self.transpose = torch.nn.Conv2d(1, 1, 1, stride=1, padding=1)
        self.dropout = torch.nn.Conv2d(1, 1, 1, stride=1, padding=1)

    def forward(self, input1, input2, input3, input4, input5):
        qk = torch.matmul(input1, input2)
        scaled_qk = qk.div(input4)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = self.dropout(softmax_qk.matmul(input3))
        return output


func = Model().to('cpu')


input1 = torch.randn(1, 1, 64, 64)

input2 = torch.randn(1, 1, 64, 64)

input3 = torch.randn(1, 1, 64, 64)
input4 = 1
input5 = 1

test_inputs = [input1, input2, input3, input4, input5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxqwinvqb/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpxqwinvqb/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpxqwinvqb', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''