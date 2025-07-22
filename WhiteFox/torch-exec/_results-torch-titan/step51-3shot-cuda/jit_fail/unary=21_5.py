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
        self.conv1 = torch.nn.Conv2d(3, 12, 1, stride=1)
        self.pool = torch.nn.MaxPool2d(7, stride=3, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v1 = torch.tanh(v1)
        v1 = self.pool(v1)
        v1 = v1.permute(0, 2, 3, 1)
        v1 = v1.contiguous().view((- 1), (15 * 8))
        v1 = torch.tanh(v1)
        return v1




func = ModelTanh().to('cuda')



x = torch.randn(64, 3, 224, 224)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 120]' is invalid for input of size 4092672

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(64, 73, 73, 12)), -1, 120), **{}):
shape '[-1, 120]' is invalid for input of size 4092672

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''