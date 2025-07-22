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
        self.conv1d1 = torch.nn.Conv1d(56, 75, 3, stride=2, padding=1)
        self.conv1d2 = torch.nn.Conv1d(56, 73, 1, stride=1, padding=1)

    def forward(self, t1, x3, t0):
        v1 = self.conv1d1(t1)
        v2 = self.conv1d2(v1)
        if t0:
            x3 = v2
        else:
            t2 = (t1 + x3)
        t3 = t2.view((- 1))
        return t1




func = Model().to('cuda')



t1 = torch.randn(25, 56, 26)



x3 = torch.randn(1, 73, 26)

t0 = 1

test_inputs = [t1, x3, t0]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [73, 56, 1], expected input[25, 75, 13] to have 56 channels, but got 75 channels instead

jit:
Failed running call_module L__self___conv1d2(*(FakeTensor(..., device='cuda:0', size=(25, 75, 13)),), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''