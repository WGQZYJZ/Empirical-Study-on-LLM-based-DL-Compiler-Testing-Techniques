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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv_1 = torch.nn.Conv2d(1, 8, 1)
        self.conv_2 = torch.nn.Conv2d(8, 8, 1)
        self.conv_3 = torch.nn.Conv2d(8, 1, 1)

    def forward(self, x1):
        x2 = self.conv_1(x1)
        x3 = self.conv_2(x2)
        x1 = torch.tanh(x3)
        x1 = self.conv_3(x1)
        return x1




func = ModelTanh().to('cuda')



x1 = torch.randn(1, 1, 28, 28)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpt4fqj4l6/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpt4fqj4l6', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpt4fqj4l6/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''