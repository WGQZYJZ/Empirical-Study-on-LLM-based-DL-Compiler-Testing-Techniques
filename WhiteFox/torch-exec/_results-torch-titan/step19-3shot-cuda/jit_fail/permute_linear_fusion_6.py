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
        self.conv1 = torch.nn.Conv2d(1, 20, 5, 1)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, 1)
        self.mp1 = torch.nn.MaxPool2d(2, 2)
        self.mp2 = torch.nn.MaxPool2d(2, 2)
        self.fc1 = torch.nn.Linear(800, 500)
        self.fc2 = torch.nn.Linear(500, 10)

    def forward(self, x):
        x = self.mp1(x)
        x = F.relu(self.conv1(x))
        x = self.mp2(x)
        x = F.relu(self.conv2(x))
        x = x.view((- 1), 800)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)




func = Model().to('cuda')



x = torch.randn(1, 1, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 800]' is invalid for input of size 50

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 50, 1, 1)), -1, 800), **{}):
shape '[-1, 800]' is invalid for input of size 50

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''