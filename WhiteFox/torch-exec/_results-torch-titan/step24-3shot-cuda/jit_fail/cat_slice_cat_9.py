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

    def forward(self, x, __input_tensor__):
        v0 = torch.cat([x, __input_tensor__], dim=1)
        v1 = torch.cat([v0], dim=1)
        return v1



func = Model().to('cuda')



x = torch.randn(20, 16, 28, 28)

__input_tensor__ = 1

test_inputs = [x, __input_tensor__]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7b0d058699e0>(*([FakeTensor(..., device='cuda:0', size=(20, 16, 28, 28)), 1],), **{'dim': 1}):
expected Tensor as element 1 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''