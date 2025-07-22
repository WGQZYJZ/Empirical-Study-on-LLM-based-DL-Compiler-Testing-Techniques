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

    def __init__(self, min_value):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(2, 3, bias=False)
        self.min_value = min_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




min_value = 0.1

func = Model(min_value).to('cuda')




x1 = torch.tensor([[1, (- 1)], [(- 1), 1]], dtype=torch.float32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'max_value'

jit:
max_value

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''