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

    def __init__(self, min_value=0.8929750293254677):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
        self.min_value = torch.Tensor([min_value])[0]

    def forward(self, x1):
        return torch.clamp_max(torch.clamp_min(self.linear(x1), self.min_value), 0.1005024975024975)



func = Model(min_value=0.8929750293254677).to('cuda')



x1 = torch.randn(20, 3)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwfw1l6xq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpwfw1l6xq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpwfw1l6xq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''