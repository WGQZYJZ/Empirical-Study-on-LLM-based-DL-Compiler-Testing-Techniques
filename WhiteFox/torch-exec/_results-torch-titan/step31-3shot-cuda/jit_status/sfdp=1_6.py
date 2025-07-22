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

    def forward(self, v1, v2):
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = v3.div(9.765625)
        v5 = v4.softmax(dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=0.3062484076194763)
        v7 = torch.matmul(v6, v2)
        return v7



func = Model().to('cuda')



v1 = torch.randn(1, 16, 256)



v2 = torch.randn(1, 2, 256)


test_inputs = [v1, v2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9qhest4o/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9qhest4o', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9qhest4o/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''