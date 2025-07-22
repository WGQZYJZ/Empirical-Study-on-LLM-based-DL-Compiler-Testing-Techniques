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
        self.conv = torch.nn.Conv2d(512, 1000, 1, stride=1, padding=0)
        self.avg_pool = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.dropout = torch.nn.Dropout(0.2)
        self.fc = torch.nn.Linear(1000, 1000)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.avg_pool(v1)
        v3 = v2.flatten(start_dim=1)
        v4 = self.dropout(v3)
        v5 = self.fc(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 512, 28, 28)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdjh5g9mp/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdjh5g9mp', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdjh5g9mp/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''