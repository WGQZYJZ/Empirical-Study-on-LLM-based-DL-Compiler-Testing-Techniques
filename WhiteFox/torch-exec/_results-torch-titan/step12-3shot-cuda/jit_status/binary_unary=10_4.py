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

    def __init__(self, hidden_size):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(in_features=16, out_features=hidden_size)
        self.linear2 = torch.nn.Linear(in_features=hidden_size, out_features=1)

    def forward(self, x):
        l1 = self.linear1(x)
        l2 = self.linear2(l1)
        l3 = l1.sigmoid()
        l4 = l2.sigmoid()
        l5 = (l3 * l4)
        return l5



hidden_size = 1
func = Model(128).to('cuda')



x = torch.randn(8, 16)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpglf95j4t/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpglf95j4t', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpglf95j4t/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''