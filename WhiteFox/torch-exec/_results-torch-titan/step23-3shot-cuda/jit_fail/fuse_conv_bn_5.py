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
        self.conv1 = torch.nn.Conv1d(2, 3, 2)
        self.conv2 = torch.nn.Conv1d(3, 2, 2)
        self.bn = torch.nn.BatchNorm1d(3)

    def forward(self, x):
        return self.bn(self.conv2(self.conv1(x)))




func = Model().to('cuda')



x = torch.randn(1, 2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 3

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1)),), **{}):
running_mean should contain 2 elements not 3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''