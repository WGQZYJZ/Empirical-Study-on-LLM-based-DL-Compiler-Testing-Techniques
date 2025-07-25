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
        self.pool1 = torch.nn.AvgPool2d(kernel_size=7, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 3, kernel_size=1, stride=1, padding=0)
        self.flatten = torch.nn.Flatten()
        self.dropout1 = torch.nn.Dropout(p=0.3)
        self.pool3 = torch.nn.MaxPool2d(kernel_size=8, stride=4, padding=0)
        self.relu1 = torch.nn.ReLU()
        self.conv3 = torch.nn.Conv2d(3, 6, kernel_size=2, stride=1, padding=0)
        self.reshape1 = torch.nn.Unflatten(dim=1, unflattened_size=(1, 90))
        self.reshape2 = torch.nn.Unflatten(dim=1, unflattened_size=(1, 10))
        self.flatten1 = torch.nn.Flatten()
        self.relu3 = torch.nn.ReLU()
        self.linear1 = torch.nn.Linear(in_features=805, out_features=635, bias=True)
        self.linear2 = torch.nn.Linear(in_features=635, out_features=5, bias=True)

    def forward(self, x):
        v0 = self.pool1(x)
        v1 = self.conv2(v0)
        v2 = self.flatten(v1)
        v3 = self.dropout1(v2)
        v4 = self.pool3(v3)
        v5 = self.relu1(v4)
        v6 = self.relu1(v5)
        v7 = self.conv3(v6)
        v8 = self.reshape1(v7)
        v9 = self.flatten1(v8)
        v10 = self.dropout1(v9)
        v11 = self.dropout1(v10)
        v12 = self.relu3(v11)
        v13 = self.linear1(v12)
        v14 = self.linear2(v13)
        v15 = torch.sigmoid(v14)
        return v14




func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
avg_pool2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___pool1(*(1,), **{}):
avg_pool2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''