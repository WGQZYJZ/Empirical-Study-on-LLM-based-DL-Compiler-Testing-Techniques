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
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x):
        v1 = self.layer(x)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3



min_value = 1
max_value = 1
func = Model(0, 1).to('cuda')



x = torch.randn(1, 784)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'layer'

jit:
layer

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''