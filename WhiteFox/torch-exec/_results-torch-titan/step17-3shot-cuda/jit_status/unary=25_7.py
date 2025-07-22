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



class Model(nn.Module):

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = nn.Linear(3, 8)
        self.negative_slope = negative_slope

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = (t1 > 0)
        t3 = (t1 * self.negative_slope)
        t4 = torch.where(t2, t1, t3)
        return t4



negative_slope = 1
func = Model(0.2).to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_thn0l39/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_thn0l39', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_thn0l39/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''