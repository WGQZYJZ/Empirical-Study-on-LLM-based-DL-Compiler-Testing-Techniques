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
        self.conv1 = torch.nn.Conv2d(3, 128, 1, stride=1, padding=1)
        self.conv1_bn = torch.nn.BatchNorm2d(128)
        self.conv2 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=1)
        self.conv2_bn = torch.nn.BatchNorm2d(64)
        self.conv3 = torch.nn.Conv2d(64, 72, 1, stride=1, padding=1)
        self.conv3_bn = torch.nn.BatchNorm2d(72)
        self.conv4 = torch.nn.Conv2d(72, 25, 1, stride=1, padding=1)
        self.conv4_bn = torch.nn.BatchNorm2d(25)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1_bn(v2)
        v4 = self.conv2(v3)
        v5 = torch.relu(v4)
        v6 = self.conv2_bn(v5)
        v7 = self.conv3(v6)
        v8 = torch.relu(v7)
        v9 = self.conv3_bn(v8)
        v10 = self.conv4(v9)
        v11 = torch.relu(v10)
        v12 = self.conv4_bn(v11)
        v13 = torch.sigmoid(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpk_ufj47w/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpk_ufj47w', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpk_ufj47w/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''