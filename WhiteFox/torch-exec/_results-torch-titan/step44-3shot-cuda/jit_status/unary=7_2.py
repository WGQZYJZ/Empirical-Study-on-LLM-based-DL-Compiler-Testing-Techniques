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

    def __init__(self, n_features):
        super().__init__()
        self.n_features = n_features
        self.linear = torch.nn.Linear(self.n_features, 2)
        self.linear_clamp = torch.nn.Linear(self.n_features, 1)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(self.linear_clamp(x1), min=0, max=6)
        v3 = (v2 + 3)
        v4 = (v1 * v3)
        return (v4 / 6)



n_features = 1
func = Model(128).to('cuda')



x1 = torch.randn(1, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpncx6z080/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpncx6z080', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpncx6z080/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''