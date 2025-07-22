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

    def forward(self, x1, x2):
        x1.add_(12)
        x2.add_(13)
        v1 = torch.mm(x1, x2)
        x2.add_(13)
        x1.sub_(42)
        v2 = torch.mm(x1, x2)
        x2.sub_(13)
        x1.sub_(42)
        x2.add_(13)
        return torch.cat([v1, v2], 1)




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp39kr3f7d/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp39kr3f7d', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp39kr3f7d/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''