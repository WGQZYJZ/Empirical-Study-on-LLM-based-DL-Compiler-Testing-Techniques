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
        self.fc_1 = torch.nn.Linear(16, 16)
        self.bn1 = torch.nn.BatchNorm1d(16)
        self.relu_1 = torch.nn.ReLU()
        self.fc_2 = torch.nn.Linear(16, 16)
        self.bn2 = torch.nn.BatchNorm1d(16)
        self.relu_2 = torch.nn.ReLU()
        self.fc_3 = torch.nn.Linear(16, 10)

    def forward(self, x):
        x = self.fc_1(x)
        x = self.bn1(x)
        x = self.relu_1(x)
        x = self.fc_2(x)
        x = self.bn2(x)
        x = self.relu_2(x)
        x = self.fc_3(x)
        return x




func = Model().to('cuda')



x = torch.randn(16, 16)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4bw48m77/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4bw48m77', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4bw48m77/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''