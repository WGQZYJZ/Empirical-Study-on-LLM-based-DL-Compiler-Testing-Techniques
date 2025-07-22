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
        self.layer2 = torch.nn.Linear(6, 4)
        self.layer3 = torch.nn.Linear(4, 1)
        self.layer4 = torch.nn.ReLU()
        self.layer5 = torch.nn.Linear(1, 3)
        self.layer6 = torch.nn.Sigmoid()
        self.layer7 = torch.nn.Linear(3, 6)

    def forward(self, x1):
        v1 = self.layer2(x1)
        v2 = self.layer3(v1)
        v3 = self.layer4(v2)
        v4 = self.layer5(v3)
        v5 = self.layer6(v4)
        v6 = self.layer7(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(2, 6)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqjh6jlek/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqjh6jlek', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqjh6jlek/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''