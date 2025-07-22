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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.model = torch.nn.Sequential(torch.nn.Linear(20, 40), torch.nn.Linear(40, 10))
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        x2 = self.model(x1)
        return (x2, x2.clamp(min=self.min_value), x2.clamp(max=self.max_value))



min_value = 1
max_value = 1
func = Model((- 20.0), 10).to('cuda')



x1 = torch.randn(1, 20)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxftbu2bx/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpxftbu2bx', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpxftbu2bx/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''