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
        self.fc1 = torch.nn.Linear(3, 5)
        self.fc2 = torch.nn.Linear(5, 6)
        self.fc3 = torch.nn.Linear(6, 7)
        self.bn1 = torch.nn.BatchNorm1d(3)
        self.bn2 = torch.nn.BatchNorm1d(5)
        self.bn3 = torch.nn.BatchNorm1d(2)

    def forward(self, x1):
        s = self.fc1(x1)
        t = self.fc2(s)
        y = self.bn2(t)
        z1 = self.bn1(x1)
        z2 = self.fc3(z1)
        return y




func = Model().to('cuda')



x = torch.randn(1, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 6 elements not 5

jit:
Failed running call_module L__self___bn2(*(FakeTensor(..., device='cuda:0', size=(1, 6)),), **{}):
running_mean should contain 6 elements not 5

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''