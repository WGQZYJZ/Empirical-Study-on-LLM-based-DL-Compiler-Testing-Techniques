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
        self.conv1 = torch.nn.Conv2d(in_channels=12, out_channels=512, kernel_size=(1, 1), stride=(1, 1), padding=0)
        self.pool1 = torch.nn.AvgPool2d(kernel_size=(1, 3))
        self.conv2 = torch.nn.Conv2d(512, 512, (1, 1), stride=(1, 1), padding=0)
        self.pool2 = torch.nn.AvgPool2d(kernel_size=(1, 3))
        self.linear1 = torch.nn.Linear(in_features=25088, out_features=11)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.pool1(v2)
        v4 = self.conv2(v3)
        v5 = torch.relu(v4)
        v6 = self.pool2(v5)
        v7 = v6.view((- 1), 25088)
        v8 = self.linear1(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 12, 275, 487)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 25088]' is invalid for input of size 7603200

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 512, 275, 54)), -1, 25088), **{}):
shape '[-1, 25088]' is invalid for input of size 7603200

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''