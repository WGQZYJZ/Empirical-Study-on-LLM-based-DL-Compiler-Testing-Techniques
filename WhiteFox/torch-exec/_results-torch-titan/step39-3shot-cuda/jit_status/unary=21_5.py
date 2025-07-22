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
        self.conv1 = torch.nn.Conv2d(31, 73, 1, padding=0, bias=False)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(73, 109, 1, padding=0, bias=False)
        self.relu2 = torch.nn.ReLU()
        self.conv3 = torch.nn.ConvTranspose2d(109, 45, 3, stride=2, padding=1, output_padding=1, bias=False)
        self.conv4 = torch.nn.Conv2d(45, 15, 1, padding=0, bias=False)

    def forward(self, x17):
        v18 = self.conv1(x17)
        v33 = self.relu1(v18)
        v34 = self.conv2(v33)
        v36 = self.relu2(v34)
        v37 = self.conv3(v36)
        v38 = self.conv4(v37)
        v39 = torch.tanh(v38)
        return v39




func = ModelTanh().to('cuda')



x17 = torch.randn(1, 31, 22, 22)


test_inputs = [x17]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsh7vegb3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpsh7vegb3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpsh7vegb3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''