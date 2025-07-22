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
        self.conv1 = torch.nn.Conv2d(3, 3, 3, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x2):
        x = self.conv2(self.conv1(x2))
        x = self.relu(x)
        x = self.relu(x)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.relu(x)
        return x[0]




func = Model().to('cuda')



x2 = torch.randn(1, 3, 5, 5)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_r786qce/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_r786qce', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_r786qce/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''