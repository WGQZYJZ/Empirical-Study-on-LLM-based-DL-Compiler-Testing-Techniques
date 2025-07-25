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
        self.conv01 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv02 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv03 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv04 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv05 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv06 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv07 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv08 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv09 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv10 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv11 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv12 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv13 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv14 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv15 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv16 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv17 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv18 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv19 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv20 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv21 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv22 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv23 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)
        self.conv24 = torch.nn.Conv1d(16, 64, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv01(x1)
        v2 = self.conv02(x1)
        v3 = self.conv03(x1)
        v4 = self.conv04(x1)
        v5 = self.conv05(x1)
        v6 = self.conv06(x1)
        v7 = self.conv07(x1)
        v8 = self.conv08(x1)
        v9 = self.conv09(x1)
        v10 = self.conv10(x1)
        v11 = self.conv11(x1)
        v12 = self.conv12(x1)
        v13 = self.conv13(x1)
        v14 = self.conv14(x1)
        v15 = self.conv15(x1)
        v16 = self.conv16(x1)
        v17 = self.conv17(x1)
        v18 = self.conv18(x1)
        v19 = self.conv19(x1)
        v20 = self.conv20(x1)
        v21 = self.conv21(x1)
        v22 = self.conv22(x1)
        v23 = self.conv23(x1)
        v24 = self.conv24(x1)
        v25 = v1 + v2 + v3 + v4 + v5 + v6 + v8 + v9 + v10 + v11 + v12 + v14 + v15 + v16 + v17 + v18 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10 + v11 + v12 + v13 + v14 + v15 + v16 + v17 + v18 + v19 + v20 + v21 + v22 + v23 + v24
        v26 = torch.relu(v25)
        return v26



func = Model().to('cuda')


x1 = torch.randn(1, 16, 1024)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf0qn38bc/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpf0qn38bc/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpf0qn38bc', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''