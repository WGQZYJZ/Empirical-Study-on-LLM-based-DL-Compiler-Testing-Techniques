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

    def forward(self, x):
        x = self.layers(x)
        y = torch.stack((x, x), dim=0)
        z = torch.stack((y, y, y), dim=0)
        q = torch.flatten(z, 1)
        q = q.reshape((1, 18))
        return q




func = Model().to('cuda')



x = torch.randn(3, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[1, 18]' is invalid for input of size 72

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(3, 24)), (1, 18)), **{}):
shape '[1, 18]' is invalid for input of size 72

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''