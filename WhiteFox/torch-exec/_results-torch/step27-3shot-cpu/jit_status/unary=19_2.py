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

    def __init__(self, num_in_feats, num_out_feats):
        super().__init__()
        self.linear = torch.nn.Linear(num_in_feats, num_out_feats)

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = torch.sigmoid(t1)
        return t2


num_in_feats = 1
num_out_feats = 1
func = Model(8, 1).to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_3nx2aw7/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_3nx2aw7/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_3nx2aw7', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''