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
        self.conv1 = torch.nn.Conv2d(91, 225, (7, 7), stride=(1, 1), padding=(3, 3))
        self.conv2 = torch.nn.Conv2d(225, 512, (1, 1), stride=(1, 1), padding=(0, 0))

    def forward(self, input):
        x1 = self.conv1(input)
        x2 = F.max_pool2d(x1, kernel_size=3, stride=2, padding=1, ceil_mode=False)
        x3 = (x2 - 1.7321)
        x4 = F.relu(x3)
        x5 = self.conv2(x4)
        x6 = F.local_response_norm(x5, size=5, alpha=0.0001, beta=0.75, k=1.0)
        return x6




func = Model().to('cuda')



input = torch.randn(1, 91, 129, 64)


test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9sbe_93x/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9sbe_93x', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9sbe_93x/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''