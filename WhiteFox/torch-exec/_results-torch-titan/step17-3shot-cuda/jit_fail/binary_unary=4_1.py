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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)

    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        v2 = (v1 + kwargs['other'])
        v3 = F.relu(v2)
        return v3



other = 1
func = Model(torch.randn(16)).to('cuda')



x1 = torch.randn(1, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'other'

jit:
other

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''