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

    def __init__(self, min_value, max_value):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value

    def forward(self, x1):
        t1 = (torch.mm(x1, self.weight) + self.bias)
        t2 = torch.clamp(t1, self.min_value)
        t3 = torch.clamp(t2, self.max_value)
        return t3



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'weight'

jit:
weight

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''