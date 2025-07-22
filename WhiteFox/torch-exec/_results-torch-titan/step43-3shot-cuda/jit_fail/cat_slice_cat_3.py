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

    def forward(self, __input1__, __input2__):
        v1 = torch.cat([__input1__, __input2__], dim=1)
        v2 = v1[:, __input1__.size(1):(- 1)]
        v3 = v2[:, 0:__input2__.size(1)]
        v4 = torch.cat([__input1__, v3], dim=1)
        return v4



func = Model().to('cuda')

__input1__ = 1
__input2__ = 1

test_inputs = [__input1__, __input2__]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x737f2c2699e0>(*([1, 1],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''