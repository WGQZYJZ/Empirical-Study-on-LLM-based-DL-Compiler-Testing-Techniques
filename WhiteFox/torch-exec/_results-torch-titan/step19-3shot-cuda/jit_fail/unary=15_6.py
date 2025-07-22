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
        self.conv = torch.nn.Conv2d(1, 128, 1, stride=1, padding=0)
        self.layernorm = torch.nn.LayerNorm((128, 19, 19))
        self.bn = torch.nn.BatchNorm2d(128)
        self.conv2 = torch.nn.Conv2d(128, 128, (5, 19), stride=1, padding=0)
        self.layernorm2 = torch.nn.LayerNorm((128, 19, 19))
        self.bn2 = torch.nn.BatchNorm2d(128)
        self.conv3 = torch.nn.Conv2d(128, 128, (19, 5), stride=1, padding=0)
        self.layernorm3 = torch.nn.LayerNorm((128, 19, 19))
        self.bn3 = torch.nn.BatchNorm2d(128)
        self.conv4 = torch.nn.Conv2d(128, 128, (19, 19), stride=1, padding=0)
        self.layernorm4 = torch.nn.LayerNorm((128, 19, 19))
        self.bn4 = torch.nn.BatchNorm2d(128)
        self.conv5 = torch.nn.Conv2d(128, 128, 1, stride=1, padding=0)
        self.layernorm5 = torch.nn.LayerNorm((128, 19, 19))
        self.bn5 = torch.nn.BatchNorm2d(128)
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.fc = torch.nn.Linear(128, 1000)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.layernorm(v1)
        v3 = self.bn(v2)
        v4 = self.conv2(v3)
        v5 = self.layernorm2(v4)
        v6 = self.bn2(v5)
        v7 = self.conv3(v6)
        v8 = self.layernorm3(v7)
        v9 = self.bn3(v8)
        v10 = self.conv4(v9)
        v11 = self.layernorm4(v10)
        v12 = self.bn4(v11)
        v13 = self.conv5(v12)
        v14 = self.layernorm5(v13)
        v15 = self.bn5(v14)
        v16 = self.gap(v15)
        v17 = torch.flatten(v16, 1)
        v18 = self.fc(v17)
        return v18




func = Model().to('cuda')



x1 = torch.randn(1, 1, 32, 1024)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given normalized_shape=[128, 19, 19], expected input with shape [*, 128, 19, 19], but got input of size[1, 128, 32, 1024]

jit:
Failed running call_module L__self___layernorm(*(FakeTensor(..., device='cuda:0', size=(1, 128, 32, 1024)),), **{}):
Given normalized_shape=[128, 19, 19], expected input with shape [128, 19, 19], but got input of size torch.Size([1, 128, 32, 1024])

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''