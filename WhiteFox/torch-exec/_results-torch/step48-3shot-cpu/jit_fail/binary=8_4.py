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
        self.conv1 = torch.nn.Conv2d(1, 64, 7, stride=2, padding=3)
        self.conv2 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1, output_padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(64, 1, 16, stride=8, padding=4, output_padding=0)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.bn2 = torch.nn.BatchNorm2d(64)
        self.relu1 = torch.nn.ReLU()
        self.relu2 = torch.nn.ReLU()
        self.relu3 = torch.nn.ReLU()
        self.relu4 = torch.nn.ReLU()
        self.tanh1 = torch.nn.Tanh()
        self.tanh2 = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.relu1(v1)
        v3 = self.conv2(v2)
        v4 = self.relu2(v3)
        v5 = self.conv3(v4)
        v6 = self.tanh2(v5)
        v7 = self.bn1(v6)
        v8 = self.relu4(v7)
        v9 = self.bn2(v8)
        v10 = torch.sigmoid(v9)
        v11 = self.tanh1(v10)
        return v11



func = Model().to('cpu')


x = torch.randn(1, 1, 256, 256)

test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 1 elements not 64

jit:
Failed running call_function <function batch_norm at 0x732cb396ce50>(*(FakeTensor(..., size=(1, 1, 2048, 2048)), FakeTensor(..., size=(64,)), FakeTensor(..., size=(64,)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), False, 0.1, 1e-05), **{}):
running_mean should contain 1 elements not 64

from user code:
   File "<string>", line 36, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''