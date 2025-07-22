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
        self.conv1 = torch.nn.Conv1d(4, 48, 7, stride=2, padding=3, bias=False)
        self.conv2 = torch.nn.Conv1d(48, 48, 3, stride=1, padding=1, bias=True)
        self.conv3 = torch.nn.Conv1d(48, 48, 3, stride=2, padding=1, bias=False)
        self.conv4 = torch.nn.Conv1d(48, 96, 3, stride=1, padding=2, bias=True)
        self.conv5 = torch.nn.Conv1d(96, 96, 1, stride=2, padding=0, bias=True)

    def forward(self, x1):
        v1 = torch.relu(self.conv1(x1))
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = torch.relu(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 4, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6eb1amaw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6eb1amaw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6eb1amaw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''