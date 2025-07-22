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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = (v1 * torch.clamp(torch.min(6), torch.max(0), (v1 + 3)))
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x2 = torch.randn(1, 3)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
min(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method min of type object at 0x75395e6699e0>(*(6,), **{}):
min(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''