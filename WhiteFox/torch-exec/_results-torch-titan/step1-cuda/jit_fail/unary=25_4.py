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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1.gt(0)
        v3 = v2.int()
        v4 = v3.add(2)
        v5 = v4.long()
        v6 = v5.sub(1)
        v7 = (v6 != 2)
        v8 = (v7 | v2)
        v9 = v8.float()
        v10 = v8.lt(0)
        v11 = (v10 - 0.5)
        v12 = (v9 & v11)
        v13 = v12.sum(0)
        v14 = v13.exp()
        output = v14.log()
        return output



func = Model().to('cuda')



x = torch.randn(1, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Subtraction, the `-` operator, with a bool tensor is not supported. If you are trying to invert a mask, use the `~` or `logical_not()` operator instead.

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzn8upxju/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzn8upxju', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzn8upxju/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''