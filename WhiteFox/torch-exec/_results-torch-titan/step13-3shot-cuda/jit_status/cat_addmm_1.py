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
        self.f_linear1 = torch.nn.Linear(((32 * 32) * 3), 256)
        self.f_linear2 = torch.nn.Linear(256, 256)

    def forward(self, img):
        flat = img.view((- 1), ((32 * 32) * 3))
        f0 = self.f_linear1(flat)
        f1 = torch.relu(f0)
        f2 = self.f_linear2(f1)
        f3 = torch.relu(f2)
        f_add = f3
        x = torch.cat([f3], dim=1)
        f_cat = x
        return (f_add, f_cat)



func = Model().to('cuda')



img = torch.randn(1, 3, 32, 32)


test_inputs = [img]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3ojabnri/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp3ojabnri', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp3ojabnri/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''