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
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, input_tensor):
        intermediate_variable_1 = self.linear(input_tensor)
        intermediate_variable_2 = intermediate_variable_1 * 0.5
        intermediate_variable_3 = intermediate_variable_1 * 0.7071067811865476
        intermediate_variable_4 = torch.erf(intermediate_variable_3)
        intermediate_variable_5 = intermediate_variable_4 + 1
        intermediate_variable_6 = intermediate_variable_2 * intermediate_variable_5
        return intermediate_variable_6


func = Model().to('cpu')


input_tensor = torch.randn((1, 5))

test_inputs = [input_tensor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjz6cx49x/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpjz6cx49x/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpjz6cx49x', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''