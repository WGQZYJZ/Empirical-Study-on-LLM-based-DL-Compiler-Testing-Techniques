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

    def __init__(self, kernel_size=[]):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=1, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=8, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=8, out_channels=4, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(in_channels=4, out_channels=10, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        for m in self.modules():
            if (type(m) == nn.Conv2d):
                m.weight.data = (m.weight.data - 99999.0)
                m.bias.data = (m.bias.data + 10000)
        v1 = self.conv1(x)
        v2 = torch.nn.functional.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.nn.functional.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.nn.functional.sigmoid(v5)
        v7 = self.conv4(v6)
        v8 = torch.nn.functional.sigmoid(v7)
        return v8




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbzosveob/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbzosveob', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbzosveob/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''