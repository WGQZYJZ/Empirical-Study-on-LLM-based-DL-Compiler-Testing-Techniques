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
        if (torch.cat([torch.mm(x1, x2)], 1) > 0):
            for loopVar2 in range(3):
                for loopVar1 in range(5):
                    v = torch.mm(x1, x2)
            return torch.cat(v, 1)
        else:
            v1 = torch.mm(x1, x2)
            return torch.cat([v1, v1], 1)




func = Model().to('cuda')



x1 = torch.randn(5, 5)



x2 = torch.randn(5, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7ajlobpb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7ajlobpb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7ajlobpb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''