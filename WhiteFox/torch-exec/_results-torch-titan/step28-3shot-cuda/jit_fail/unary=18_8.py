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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.pool1 = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(8, 8, 3)
        self.pool2 = torch.nn.MaxPool2d(2, 2)
        self.out = torch.nn.Linear(10, 4)

    def forward(self, x1):
        v1 = self.pool1(torch.sigmoid(self.conv1(x1)))
        v2 = self.pool2(torch.sigmoid(self.conv2(v1)))
        v3 = v2.view((- 1), 4, 24)
        v4 = torch.sigmoid(self.out(v3))
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 4, 24]' is invalid for input of size 24200

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 8, 55, 55)), -1, 4, 24), **{}):
shape '[-1, 4, 24]' is invalid for input of size 24200

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''