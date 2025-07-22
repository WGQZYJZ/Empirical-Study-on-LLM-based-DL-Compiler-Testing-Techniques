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

    def __init__(self, linear_input_size=8, linear_output_size=8):
        super().__init__()
        self.linear = torch.nn.Linear(linear_input_size, linear_output_size)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if (other == None):
            return v1
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 8)



x2 = torch.randn(1, 8)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9sg_gfbd/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9sg_gfbd', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9sg_gfbd/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''