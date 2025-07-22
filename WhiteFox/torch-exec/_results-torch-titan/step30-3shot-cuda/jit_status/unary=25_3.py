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
        self.linear1 = torch.nn.Linear(89, 1028)
        self.linear2 = torch.nn.Linear(1028, 1152)
        self.fc = torch.nn.Linear(1152, 5)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 > 0)
        v3 = (v1 * 0.01)
        v4 = torch.where(v2, v1, v3)
        t1 = self.linear2(v4)
        t2 = (t1 > 0)
        t3 = (t1 * 0.01)
        t4 = torch.where(t2, t1, t3)
        f1 = self.fc(t4)
        return f1



func = Model().to('cuda')



x1 = torch.randn(1, 89)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdec9pz37/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdec9pz37', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdec9pz37/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''