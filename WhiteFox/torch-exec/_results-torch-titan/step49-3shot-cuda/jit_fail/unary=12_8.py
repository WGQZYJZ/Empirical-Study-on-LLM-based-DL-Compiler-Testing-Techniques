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



class MyModule(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 7)
        self.norm1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, 3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(128, 128, 3, stride=2, padding=1)
        self.fc = nn.Linear(2048, 256)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(self.norm1(x), 3, stride=2)
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 3, stride=2)
        x = x.view((- 1), 2048)
        x = F.relu(self.fc(x))
        return x




func = MyModule().to('cuda')



x = torch.randn(1, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 2048]' is invalid for input of size 21632

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 128, 13, 13)), -1, 2048), **{}):
shape '[-1, 2048]' is invalid for input of size 21632

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''