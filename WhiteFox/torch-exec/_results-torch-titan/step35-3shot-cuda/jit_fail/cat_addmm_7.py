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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(16, 16)
        self.layers2 = nn.Linear(16, 32)
        self.layers3 = nn.Linear(32, 32)
        self.layers4 = nn.Linear(64, 64)

    def forward(self, x1, x2, x3, x4):
        x1 = self.layers(x1)
        x2 = self.layers2(x2)
        x3 = self.layers3(x3)
        x4 = self.layers4(x4)
        x3 = torch.cat([x3], dim=2)
        x3 = torch.stack([x3])
        x3 = x3.repeat(2, 3, 1)
        x1 = torch.cat([x1, x2, x3], dim=0)
        x4 = torch.stack([x4])
        x4 = x4.repeat(1, 3, 1)
        x5 = torch.cat([x4], dim=0)
        x6 = torch.cat([x5], dim=0)
        return (x1, x6)




func = Model().to('cuda')



x1 = torch.randn(1, 16)



x2 = torch.randn(1, 16)



x3 = torch.randn(1, 32)



x4 = torch.randn(1, 64)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method cat of type object at 0x7806e0a699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 32))],), **{'dim': 2}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''