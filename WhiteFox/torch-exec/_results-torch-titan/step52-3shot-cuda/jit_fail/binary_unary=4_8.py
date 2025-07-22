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

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        d2 = {'a': x2}
        v2 = ((v1 + x2), d2)
        v3 = F.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 8)



x2 = torch.randn(1, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
relu(): argument 'input' (position 1) must be Tensor, not tuple

jit:
Failed running call_function <function relu at 0x7de4642a0ca0>(*((FakeTensor(..., device='cuda:0', size=(1, 8)), {'a': FakeTensor(..., device='cuda:0', size=(1, 8))}),), **{}):
relu(): argument 'input' (position 1) must be Tensor, not tuple

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''