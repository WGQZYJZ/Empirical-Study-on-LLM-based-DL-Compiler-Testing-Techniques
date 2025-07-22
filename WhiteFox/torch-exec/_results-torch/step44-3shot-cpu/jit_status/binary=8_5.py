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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.conv5 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(8)
        self.bn4 = torch.nn.BatchNorm2d(8)
        self.conv7 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv8 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn5 = torch.nn.BatchNorm2d(8)
        self.bn6 = torch.nn.BatchNorm2d(8)
        self.conv9 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv10 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn7 = torch.nn.BatchNorm2d(8)
        self.bn8 = torch.nn.BatchNorm2d(8)
        self.conv11 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv12 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn9 = torch.nn.BatchNorm2d(8)
        self.bn10 = torch.nn.BatchNorm2d(8)
        self.conv13 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.conv14 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=1)
        self.bn11 = torch.nn.BatchNorm2d(8)
        self.bn12 = torch.nn.BatchNorm2d(8)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.bn1(v1)
        v4 = self.bn2(v2)
        v5 = v3 + v4
        v6 = self.conv3(v5)
        v7 = self.conv4(v5)
        v8 = self.bn3(v6)
        v9 = self.bn4(v7)
        v10 = v8.mul(v9)
        v11 = self.conv5(v10)
        v12 = self.conv6(v10)
        v13 = self.bn5(v11)
        v14 = self.bn6(v12)
        v15 = v13 - v14
        v16 = self.conv7(v15)
        v17 = self.conv8(v15)
        v18 = self.bn7(v16)
        v19 = self.bn8(v17)
        v20 = v18.add(v19)
        v21 = self.conv9(v20)
        v22 = self.conv10(v20)
        v23 = self.bn9(v21)
        v24 = self.bn10(v22)
        v25 = v23.div(v24)
        v26 = self.conv11(v25)
        v27 = self.conv12(v25)
        v28 = self.bn11(v26)
        v29 = self.bn12(v27)
        v30 = v28.mul_(v29)
        v31 = self.conv13(v30)
        v32 = self.conv14(v30)
        v34 = v31 - v32
        return v34



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(1, 3, 32, 32)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpiaxhgeks/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpiaxhgeks/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpiaxhgeks', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''