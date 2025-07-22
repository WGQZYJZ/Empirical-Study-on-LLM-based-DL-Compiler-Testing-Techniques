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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)
        self.conv9 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)
        self.conv10 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=0)
        self.conv11 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv12 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v1)
        v4 = torch.relu(v2)
        v5 = self.conv3(v1)
        v6 = torch.relu(v2)
        v7 = self.conv4(v4)
        v8 = torch.relu(v7)
        v9 = self.conv5(v4)
        v10 = torch.relu(v7)
        v11 = self.conv6(v9)
        v12 = torch.relu(v11)
        v13 = self.conv7(v8)
        v14 = torch.relu(v13)
        v15 = self.conv8(v12)
        v16 = torch.relu(v15)
        v17 = self.conv9(v16)
        v18 = torch.relu(v17)
        v19 = self.conv10(v18)
        v20 = torch.relu(v19)
        v21 = self.conv11(v19)
        v22 = torch.relu(v21)
        v23 = self.conv12(v22)
        v24 = torch.relu(v23)
        return v24




func = Model().to('cuda')



x1 = torch.randn(4, 3, 256, 256)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx9885bcx/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpx9885bcx', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpx9885bcx/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''