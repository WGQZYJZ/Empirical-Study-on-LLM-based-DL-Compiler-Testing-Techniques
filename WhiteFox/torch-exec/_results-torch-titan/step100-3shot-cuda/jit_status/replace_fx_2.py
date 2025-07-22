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
        self.dropout_p = 0.2

    def forward(self, input):
        t1 = torch.rand_like(input)
        t1 += 0.0033333333
        t2 = torch.zeros_like(t1)
        t2 += 0.11535001535000937
        m = (torch.rand_like(t2) < self.dropout_p)
        t2 = torch.where(m, t1, t2)
        output = torch.clip(t2, max=1.0)
        return output




func = Model().to('cuda')




input = torch.rand_like(torch.ones(10, 10))


test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl55i0m70/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl55i0m70', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl55i0m70/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''