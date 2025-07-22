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
        self.layers = nn.Linear(3, 10)
        self.batch_norm = nn.BatchNorm1d(5)

    def forward(self, x):
        x = self.layers(x)
        x = torch.cat((x, x, x, x), dim=1)
        x = self.batch_norm(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
running_mean should contain 40 elements not 5

jit:
Failed running call_module L__self___batch_norm(*(FakeTensor(..., device='cuda:0', size=(2, 40)),), **{}):
running_mean should contain 40 elements not 5

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''