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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.n1 = torch.nn.LayerNorm(8)
        self.n2 = torch.nn.InstanceNorm2d(8, affine=True)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = v1 + v2
        v4 = self.n1(v3)
        v5 = self.bn2(v3)
        v6 = self.n2(v5)
        v7 = torch.sigmoid(v6)
        v8 = self.conv3(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given normalized_shape=[8], expected input with shape [*, 8], but got input of size[1, 8, 66, 66]

jit:
Failed running call_function <function layer_norm at 0x732cb3971040>(*(FakeTensor(..., size=(1, 8, 66, 66)), (8,), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), 1e-05), **{}):
Given normalized_shape=[8], expected input with shape [8], but got input of size torch.Size([1, 8, 66, 66])

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/normalization.py", line 217, in forward
    return F.layer_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''