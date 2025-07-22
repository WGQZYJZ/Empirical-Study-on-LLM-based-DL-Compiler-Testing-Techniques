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
        self.sigmoid = torch.nn.Sigmoid()
        self.convs = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[3, 9], stride=5, padding=2)
        self.conv_7 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1, groups=1, bias=False, dilation=1)
        self.bn_7 = torch.nn.BatchNorm2d(64)
        self.conv_8 = torch.nn.Conv2d(64, 128, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_8 = torch.nn.BatchNorm2d(128)
        self.conv_13 = torch.nn.Conv2d(128, 224, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_13 = torch.nn.BatchNorm2d(224)
        self.conv_14 = torch.nn.Conv2d(224, 128, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_14 = torch.nn.BatchNorm2d(128)
        self.conv_19 = torch.nn.Conv2d(128, 32, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_19 = torch.nn.BatchNorm2d(32)
        self.conv_20 = torch.nn.Conv2d(32, 128, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_20 = torch.nn.BatchNorm2d(128)
        self.conv_21 = torch.nn.Conv2d(128, 197, 1, stride=1, padding=0, groups=1, bias=False, dilation=1)
        self.bn_21 = torch.nn.BatchNorm2d(197)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv_7(x)
        v2 = self.bn_7(v1)
        v3 = self.sigmoid(v2)
        v4 = torch.mul(v3, x)
        v5 = self.conv_8(v4)
        v6 = self.bn_8(v5)
        v7 = self.sigmoid(v6)
        v8 = torch.mul(v7, v4)
        v9 = self.conv_13(v8)
        v10 = self.bn_13(v9)
        v11 = self.sigmoid(v10)
        v12 = torch.mul(v11, v8)
        v13 = self.conv_14(v12)
        v14 = self.bn_14(v13)
        v15 = self.sigmoid(v14)
        v16 = torch.mul(v15, v12)
        v17 = self.conv_19(v16)
        v18 = self.bn_19(v17)
        v19 = self.sigmoid(v18)
        v20 = torch.mul(v19, v16)
        v21 = self.conv_20(v20)
        v22 = self.bn_20(v21)
        v23 = self.sigmoid(v22)
        res0 = torch.mul(v23, v20)
        v27 = self.conv_21(res0)
        v28 = self.bn_21(v27)
        v29 = self.sigmoid(v28)
        v30 = self.tanh(v29)
        v31 = torch.mul(v30, res0)
        return v31




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 112, 112)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method mul of type object at 0x7936fb0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 112, 112)), FakeTensor(..., device='cuda:0', size=(1, 3, 112, 112))), **{}):
Attempting to broadcast a dimension of length 3 at -3! Mismatching argument at index 1 had torch.Size([1, 3, 112, 112]); but expected shape should be broadcastable to [1, 64, 112, 112]

from user code:
   File "<string>", line 41, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''