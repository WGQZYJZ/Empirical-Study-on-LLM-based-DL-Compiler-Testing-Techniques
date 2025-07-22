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
        self.conv1 = torch.nn.Conv1d(8, 8, 1)
        self.bn = torch.nn.BatchNorm1d(8)
        self.avg_pool = torch.nn.AdaptiveAvgPool1d(4)

    def forward(self, x):
        x = torch.nn.functional.relu(self.conv1(x))
        x = self.bn(x)
        y = self.avg_pool(x)
        return y




func = Model().to('cuda')



x = torch.randn(1, 8, 16)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplbrxb7ef/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplbrxb7ef', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplbrxb7ef/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''