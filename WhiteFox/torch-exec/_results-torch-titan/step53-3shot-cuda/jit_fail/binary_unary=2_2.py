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
        self.conv1 = torch.nn.Conv2d(12, 3, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.permute(v1, 0, 2, 3, 1)
        v3 = (v2 - 299)
        v4 = F.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 12, 10, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute() takes 2 positional arguments but 5 were given

jit:
Failed running call_function <built-in method permute of type object at 0x7b3e3a2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 10, 10)), 0, 2, 3, 1), **{}):
permute() takes 2 positional arguments but 5 were given

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''