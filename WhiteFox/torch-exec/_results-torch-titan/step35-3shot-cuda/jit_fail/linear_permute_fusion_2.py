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
        y = torch.randperm(1)
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.chunk(1, dim=(y - 1))
        return v2[0].squeeze(dim=(- 2))




func = Model().to('cuda')



x1 = torch.rand(2, 2, 2, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
chunk(): argument 'dim' must be int, not Tensor

jit:
Failed running call_method chunk(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2, 2, 2, 2)), 1), **{'dim': FakeTensor(..., size=(1,), dtype=torch.int64)}):
chunk(): argument 'dim' must be int, not FakeTensor

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''