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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 * torch.clamp(torch.minimum(torch.maximum((v1 + 3), 0), 6)))
        v3 = (v2 / 6)
        return (v3 * scale)



func = Model().to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
maximum(): argument 'other' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method maximum of type object at 0x77639fa699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8)), 0), **{}):
maximum(): argument 'other' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''