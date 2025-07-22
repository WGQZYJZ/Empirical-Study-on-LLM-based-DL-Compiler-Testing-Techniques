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
        self.layer1 = torch.nn.Conv2d(5, 5, 2)
        self.layer2 = torch.nn.BatchNorm2d(5)
        self.layer3 = torch.nn.Conv2d(5, 5, 2)

    def forward(self, x3):
        x1 = self.layer1(x3)
        x4 = self.layer2(x1)
        x2 = self.layer3(x4)
        return (x1, x2, x4)




func = Model().to('cuda')



x3 = torch.randn(1, 5, 4, 4)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpydfdp227/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpydfdp227', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpydfdp227/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''