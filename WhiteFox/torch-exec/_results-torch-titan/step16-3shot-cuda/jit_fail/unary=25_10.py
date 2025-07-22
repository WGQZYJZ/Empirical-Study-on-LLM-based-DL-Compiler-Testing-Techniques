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

    def __init__(self, slope):
        super().__init__()
        self.slope = slope

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.conv.weight)
        v2 = (v1 > 0)
        v3 = (v1 * self.slope)
        v4 = torch.where(v2, v1, v3)
        return v4



slope = 1
func = Model(0.1).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv'

jit:
conv

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''