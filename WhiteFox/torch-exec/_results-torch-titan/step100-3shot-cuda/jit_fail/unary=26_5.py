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
        self.conv_t = torch.nn.ConvTranspose2d(95, 95, 4, stride=2, padding=1, output_padding=3, bias=False)

    def forward(self, x8):
        q0 = self.conv_t(x8)
        q1 = (q0 > 0)
        q2 = (q0 * (- 0.928))
        q3 = torch.where(q1, q0, q2)
        return q3




func = Model().to('cuda')



x8 = torch.randn(1, 95, 16, 17)


test_inputs = [x8]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 3 output_padding_width: 3 stride_height: 2 stride_width: 2 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpemfvkbv4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpemfvkbv4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpemfvkbv4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''