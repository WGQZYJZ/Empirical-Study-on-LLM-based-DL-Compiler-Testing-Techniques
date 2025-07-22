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
        self.linear = torch.nn.Linear(64, 64)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + other)
        return v3



other = 1
func = Model(torch.rand(64)).to('cuda')



x1 = torch.rand(1, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'v3' is not defined

jit:
name 'v3' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''