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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.flatten_module = nn.Flatten()
        self.linear_module = nn.Linear(((16 * 7) * 7), 50)
        self.leakyrelu_module = nn.LeakyReLU()
        self.linear_module_1 = nn.Linear(50, 20)
        self.linear_module_2 = nn.Linear(20, 8)
        self.linear_module_3 = nn.Linear(8, 2)
        self.softmax_module = nn.Softmax()

    def forward(self, images):
        flatten_res = self.flatten_module(images)
        linear_res = self.linear_module(flatten_res)
        relu_res = self.leakyrelu_module(linear_res)
        linear_res = self.linear_module_1(relu_res)
        linear_res = self.linear_module_2(linear_res)
        linear_res = self.linear_module_3(linear_res)
        sm_res = self.softmax_module(linear_res)
        return sm_res




func = Model().to('cuda')



x1 = torch.randn(1, 28, 28)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8ms93o54/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8ms93o54', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8ms93o54/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''