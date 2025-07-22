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

    def __init__(self, min_value=(- 111.3), max_value=(- 80.3), padding=2, kernel_size=3):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 5, kernel_size, stride=2, padding=padding)
        self.act_3 = torch.nn.ReLU(inplace=True)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x7):
        v5 = self.conv_transpose2d(x7)
        v9 = self.min_value
        v12 = self.act_3(v5)
        v14 = self.max_value
        v16 = torch.clamp(v12, min=v9)
        v18 = torch.clamp(v16, max=v14)
        return v18




func = Model().to('cuda')



x7 = torch.randn(1, 3, 13, 13)


test_inputs = [x7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp47mtscrt/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp47mtscrt', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp47mtscrt/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''