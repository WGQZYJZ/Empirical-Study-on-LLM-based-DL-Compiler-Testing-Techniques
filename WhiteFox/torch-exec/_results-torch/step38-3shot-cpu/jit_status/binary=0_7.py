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

    def forward(self, x1, other1, other2=0, other3=0, other4=0, other5=0, other6=0, other7=0, other8=0, other9=0, other10=0, other11=0, other12=0, other13=0, other14=0, other15=0, other16=0, other17=0, other18=0, other19=0, other20=0, other21=0):
        v1 = x1 + other1
        v2 = x1 + other2
        v3 = x1 + other3
        v4 = x1 + other4
        v5 = x1 + other5
        v6 = x1 + other6
        v7 = x1 + other7
        v8 = x1 + other8
        v9 = x1 + other9
        v10 = x1 + other10
        v11 = x1 + other11
        v12 = x1 + other12
        v13 = x1 + other13
        v14 = x1 + other14
        v15 = x1 + other15
        v16 = x1 + other16
        v17 = x1 + other17
        v18 = x1 + other18
        v19 = x1 + other19
        v20 = x1 + other20
        v21 = x1 + other21
        return (v19, v2, v3, other3)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)
other1 = 1

test_inputs = [x1, other1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpviemy0sn/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpviemy0sn/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpviemy0sn', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''