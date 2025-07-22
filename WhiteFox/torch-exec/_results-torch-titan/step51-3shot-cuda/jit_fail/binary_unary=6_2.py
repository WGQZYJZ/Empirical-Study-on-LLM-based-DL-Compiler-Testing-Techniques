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

    def __init__(self, other_value):
        super().__init__()
        self.linear = torch.nn.Linear(6, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - self.other_value)
        v3 = torch.relu(v2)
        return v3



other_value = 1

func = Model(other_value).to('cuda')



x1 = torch.randn(1, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'other_value'

jit:
other_value

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''