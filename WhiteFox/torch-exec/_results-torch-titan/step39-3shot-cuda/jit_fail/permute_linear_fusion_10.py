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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.detach()
        v4 = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)
        v5 = torch.sum(torch.nn.functional.softsign(v4, (- 1.0), 1.0))
        v2 = (v2 + v5.unsqueeze(dim=(- 1)))
        x2 = torch.nn.functional.relu(v2)
        v5 = torch.max(x2, dim=(- 1))[0]
        v4 = v5.unsqueeze(dim=(- 1))
        v5 = (v5 + v4.to(v5.dtype))
        v4 = (v5 == (- 1)).to(v5.dtype)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
softsign() takes 1 positional argument but 3 were given

jit:
Failed running call_function <function softsign at 0x7ebfd1da2280>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 1)), -1.0, 1.0), **{}):
softsign() takes 1 positional argument but 3 were given

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''