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



class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, 3, 1, 0)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, 1, 0)
        self.conv3 = torch.nn.Conv2d(64, 128, 3, 1, 0)
        self.conv4 = torch.nn.Conv2d(128, 256, 3, 1, 0)
        self.conv5 = torch.nn.Conv2d(256, 512, 3, 1, 0)
        self.conv6 = torch.nn.Conv2d(512, 512, 3, 1, 0)
        self.linear = torch.nn.Linear(10, 100)
        self.linear2 = torch.nn.Linear(100, 10)
        self.relu = torch.nn.ReLU()
        self.max_pool2d = torch.nn.MaxPool2d(2)
        self.dropout = torch.nn.Dropout(0.5)
        self.flatten = torch.nn.Flatten()
        self.sigmoid = torch.nn.Sigmoid()
        self.avg = torch.nn.AdaptiveAvgPool2d((1, 128))

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.max_pool2d(x)
        x = self.dropout(x)
        x = self.conv3(x)
        x = self.relu(x)
        x = self.conv4(x)
        x = self.relu(x)
        x = self.max_pool2d(x)
        x = self.dropout(x)
        x = self.conv5(x)
        x = self.relu(x)
        x = self.conv6(x)
        x = self.relu(x)
        x = self.max_pool2d(x)
        x = self.flatten(x)
        x = self.linear(x)
        x = self.relu(x)
        x = torch.cat((x, (0.5 * x)), 1)
        x = self.linear2(x)
        x = self.sigmoid(x)
        x = self.avg(x)
        x = self.softmax(x)
        return x



func = MyModel().to('cuda')



x = torch.randn(512, 3, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 1, 3, 3], expected input[512, 3, 10, 10] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(512, 3, 10, 10)),), **{}):
Given groups=1, weight of size [32, 1, 3, 3], expected input[512, 3, 10, 10] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''