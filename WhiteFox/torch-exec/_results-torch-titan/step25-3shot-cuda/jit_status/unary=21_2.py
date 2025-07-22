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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.model = torch.nn.Sequential(torch.nn.Conv2d(8, 64, 3, stride=1, padding=1, bias=False), torch.nn.BatchNorm2d(64), torch.nn.ReLU(inplace=True), torch.nn.Conv2d(64, 64, 3, stride=1, padding=1, bias=True), torch.nn.Dropout2d(0.3), torch.nn.BatchNorm2d(64), torch.nn.ReLU(inplace=True), torch.nn.Conv2d(64, 1, 1, stride=1, padding=1, bias=True), torch.nn.Sigmoid())

    def forward(self, x):
        x = self.model(x)
        return x




func = ModelTanh().to('cuda')



x = torch.randn(1, 8, 32, 32)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpelxb29b0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpelxb29b0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpelxb29b0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''