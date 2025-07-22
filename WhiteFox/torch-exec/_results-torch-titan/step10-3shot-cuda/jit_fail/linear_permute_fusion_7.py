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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(torch.reshape(x1, (1, 2, 2)), torch.reshape(self.linear.weight, (2, 2)), torch.reshape(self.linear.bias, 2))
        v2 = v1.permute(0, 2, 1)
        return torch.reshape(v2, (2, 2, 2))




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
reshape(): argument 'shape' (position 2) must be tuple of ints, not int

jit:
Failed running call_function <built-in method reshape of type object at 0x768d1de699e0>(*(Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True)), 2), **{}):
reshape(): argument 'shape' (position 2) must be tuple of ints, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''