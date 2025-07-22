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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(2, 4)

    def forward(self, x):
        x = self.layers(x)
        x_1 = x.unsqueeze(1)
        x_2 = x.unsqueeze(0)
        x = (x_1 + x_2)
        (x_1, x_2) = torch.chunk(x, 2, dim=0)
        (x_1, _) = torch.chunk(x_1, 2, 1)
        (x_2, _) = torch.chunk(x_2, 2, 1)
        x = torch.cat((x_1, x_2), dim=0)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2).float()


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp914lmk4e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp914lmk4e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp914lmk4e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''