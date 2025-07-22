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

    def forward(self, x1, x2, x3):
        v1 = torch.cat((x1, x2), dim=1)
        v2 = torch.cat((v1, x3), dim=1)
        v3 = torch.cat((v2, x3), dim=1)
        v4 = torch.cat((v3, x3), dim=1)
        y = torch.relu(v4)
        return y




func = Model().to('cuda')



x1 = torch.randn(2, 2)



x2 = torch.randn(2, 3)



x3 = torch.randn(2, 2)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb3e0wjs_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpb3e0wjs_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpb3e0wjs_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''