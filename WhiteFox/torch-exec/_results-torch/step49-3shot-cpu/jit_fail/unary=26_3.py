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

class MyModel(nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.c1 = nn.ConvTranspose2d(19, 48, (8, 6), 1, (3, 2), 1)

    def forward(self, x14):
        r1 = self.c1(x14)
        r2 = r1 > 0
        r3 = r1 * 0.105
        r4 = torch.where(r2, r1, r3)
        return torch.nn.functional.adaptive_avg_pool2d(torch.nn.functional.relu(r4), 5)



func = MyModel().to('cpu')


x14 = torch.randn(487, 19, 17, 9)

test_inputs = [x14]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp57eqym5e/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp57eqym5e/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp57eqym5e', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''