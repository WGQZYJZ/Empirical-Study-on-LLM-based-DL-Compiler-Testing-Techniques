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
        self.conv1 = torch.nn.Conv2d(1, 4, 5, stride=1, padding=2)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = (v1 + x2)
        v3 = (v1 + x3)
        return (v2, v3)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 56, 56)



x2 = torch.randn(1, 1, 56, 56)



x3 = torch.randn(1, 1, 56, 56)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz4n3znml/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz4n3znml', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz4n3znml/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''