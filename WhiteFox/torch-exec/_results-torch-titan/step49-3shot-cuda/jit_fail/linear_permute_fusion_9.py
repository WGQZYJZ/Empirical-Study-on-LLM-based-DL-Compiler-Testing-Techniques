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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x2):
        v2 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        v3 = v2.permute(0, 2, 1)
        lstm2 = torch.nn.LSTM(2, 2)
        v4 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        v5 = lstm2(v4.permute(1, 0, 2))
        return v5[0]




func = Model().to('cuda')



x2 = torch.randn(1, 3, 2)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 2x2)

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0_zqk52j/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0_zqk52j', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0_zqk52j/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''