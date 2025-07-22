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

    def forward(self, x1, other=None):
        input_tensor = (x1, other)
        v1 = self.linear(input_tensor)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3)



other = torch.randn(1, 8)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not tuple

jit:
Failed running call_module L__self___linear(*((FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., device='cuda:0', size=(1, 8))),), **{}):
linear(): argument 'input' (position 1) must be Tensor, not tuple

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''