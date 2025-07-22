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

    def __init__(self, input_size, output_size):
        super().__init__()
        self.output_size = output_size
        self.weight = torch.nn.Parameter(torch.randn((input_size, output_size)))

    def forward(self, x):
        y = torch.matmul(x, self.weight)
        z = torch.nn.functional.softmax(y, dim=(- 1))
        return z




input_size = 3


output_size = 5

func = Model(input_size, output_size).to('cuda')



x = torch.randn(4, 3)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4bkckd1y/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4bkckd1y', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4bkckd1y/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''