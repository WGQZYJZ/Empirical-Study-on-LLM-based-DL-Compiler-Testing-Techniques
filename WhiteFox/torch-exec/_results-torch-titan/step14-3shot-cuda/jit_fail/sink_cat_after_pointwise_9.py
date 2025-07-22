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

    def forward(self, x, target, weight):
        x = ((x * target.max(1)[0].reshape((- 1), 1, 1)) * weight)
        return x




func = Model().to('cuda')



x = torch.randn(1)



target = torch.randn(1)



weight = torch.randn(1)


test_inputs = [x, target, weight]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_method max(*(FakeTensor(..., device='cuda:0', size=(1,)), 1), **{}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''