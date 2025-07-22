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
        self.linear = torch.nn.Linear(32, 32)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + other)
        v3 = relu(v2)
        return v3



other = 1
func = Model(torch.randn(1, 32)).to('cuda')



x = torch.randn(1, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
name 'relu' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''