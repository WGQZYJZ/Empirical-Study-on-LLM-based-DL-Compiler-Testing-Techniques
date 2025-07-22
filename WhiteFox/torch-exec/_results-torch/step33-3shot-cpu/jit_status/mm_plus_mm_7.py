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

    def forward(self, model_input):
        t1 = torch.mm(model_input, model_input)
        t2 = torch.mm(model_input, model_input)
        t3 = torch.mm(model_input, model_input)
        t4 = torch.mm(model_input, model_input)
        t5 = torch.mm(model_input, model_input)
        t6 = torch.mm(model_input, model_input)
        t7 = torch.mm(model_input, model_input)
        t8 = torch.mm(model_input, model_input)
        t9 = torch.mm(model_input, model_input)
        t10 = torch.mm(model_input, model_input)
        t11 = torch.mm(model_input, model_input)
        t12 = torch.mm(model_input, model_input)
        t13 = torch.mm(model_input, model_input)
        t14 = torch.mm(model_input, model_input)
        t15 = torch.mm(model_input, model_input)
        t16 = torch.mm(model_input, model_input)
        t17 = torch.mm(model_input, model_input)
        t18 = torch.mm(model_input, model_input)
        t19 = torch.mm(model_input, model_input)
        t20 = torch.mm(model_input, model_input)
        return t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 + t12 + t13 + t14 + t15 + t16 + t17 + t18 + t19 + t20



func = Model().to('cpu')


model_input = torch.randn(1000, 1000)

test_inputs = [model_input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_rrp5akm/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_rrp5akm/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_rrp5akm', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''