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
        self.conv1 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=5, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=5, stride=1, padding=2)
        self.conv4 = torch.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=9, stride=1, padding=4)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = torch.sigmoid(v4)
        v6 = self.conv4(v5)
        v7 = torch.dropout(v6, p=0.3)
        return torch.sigmoid(v7)




func = Model().to('cuda')



x1 = torch.randn(1, 32, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout() missing 1 required positional arguments: "train"

jit:
Failed running call_function <built-in method dropout of type object at 0x70673dc699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 256, 224, 224)),), **{'p': 0.3}):
dropout() missing 1 required positional arguments: "train"

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''