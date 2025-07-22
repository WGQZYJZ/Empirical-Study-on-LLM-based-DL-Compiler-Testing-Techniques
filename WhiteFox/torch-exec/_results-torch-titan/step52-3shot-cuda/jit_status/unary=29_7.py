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

    def __init__(self, min_value=45.49, max_value=176.31):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(5, 5, 3, stride=2, padding=2, dilation=3)
        self.act_0 = torch.nn.ReLU6()
        self.act_3 = torch.nn.ReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v10 = self.conv2d(x1)
        v12 = torch.clamp_min(v10, self.min_value)
        v15 = self.act_0(v12)
        v16 = torch.clamp_max(v15, self.max_value)
        v18 = self.act_3(v16)
        return v18




func = Model().to('cuda')



x1 = torch.randn(1, 5, 8, 8)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxwpai8p9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpxwpai8p9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpxwpai8p9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''