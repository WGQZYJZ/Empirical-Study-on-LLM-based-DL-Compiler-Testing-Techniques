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
        self.layers = nn.Linear(2, 4)
        self.layers2 = nn.Linear(2, 4)

    def forward(self, x, y):
        x = self.layers(x)
        x = torch.stack((x, x), dim=1)
        y = self.layers2(y)
        y = torch.stack((y, y), dim=1)
        z = (x + y)
        z = z.view(41, 1, 1)
        return z




func = Model().to('cuda')



x = torch.randn(1, 2)



y = torch.randn(100, 2)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
shape '[41, 1, 1]' is invalid for input of size 800

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(100, 2, 4)), 41, 1, 1), **{}):
shape '[41, 1, 1]' is invalid for input of size 800

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''