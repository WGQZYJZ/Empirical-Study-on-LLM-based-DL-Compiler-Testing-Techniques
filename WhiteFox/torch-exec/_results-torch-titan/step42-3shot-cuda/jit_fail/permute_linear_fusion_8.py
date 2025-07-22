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
        self.linear1 = torch.nn.Linear(2, 1)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1.permute(0, 2, 1), self.linear1.weight, self.linear1.bias)
        x3 = torch.nn.functional.relu(v2)
        x4 = torch.nn.functional.hardtanh(x2)
        v1 = torch.max(x1, dim=(- 1))[0]
        v3 = v1.unsqueeze(dim=(- 1))
        v3 = (v3 + v4.to(v3.dtype))
        v4 = (v3 == (- 1)).to(v3.dtype)
        v4 = torch.nn.functional.linear(v4, self.linear2.weight, self.linear2.bias)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'x2' is not defined

jit:
name 'x2' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''