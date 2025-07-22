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
        self.embedding = torch.nn.Embedding(10, 5)
        self.bn = torch.nn.BatchNorm1d(15)

    def forward(self, x1, x2):
        x1 = self.embedding(x1)
        x2 = self.bn(x2)
        return torch.cat([x1, x2], (- 1))




func = Model().to('cuda')



x1 = torch.randint(9, (4,))



x2 = torch.randn(4, 3, 5)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
running_mean should contain 3 elements not 15

jit:
Failed running call_module L__self___bn(*(FakeTensor(..., device='cuda:0', size=(4, 3, 5)),), **{}):
running_mean should contain 3 elements not 15

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''