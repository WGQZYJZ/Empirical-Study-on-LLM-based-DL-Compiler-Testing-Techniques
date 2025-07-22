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
        super(Model, self).__init__()
        self.conv_t1 = torch.nn.ConvTranspose1d(35, 91, 2, stride=2, padding=1)
        self.conv_t2 = torch.nn.ConvTranspose1d(12, 23, 4, stride=4, padding=2, output_padding=3)

    def forward(self, x4, x12):
        v2_1 = self.conv_t1(x12)
        v4 = torch.where((v2_1 > (- 1.958)), v2_1, (v2_1 * 0.24))
        v2_2 = self.conv_t2(x4)
        v5 = torch.where((v2_2 > 0.763), v2_2, (v2_2 * (- 0.051)))
        return (v4, v5)




func = Model().to('cuda')



x4 = torch.randn(2, 12, 16)



x12 = torch.randn(1, 35, 40)


test_inputs = [x4, x12]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgzqh7dkb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgzqh7dkb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgzqh7dkb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''