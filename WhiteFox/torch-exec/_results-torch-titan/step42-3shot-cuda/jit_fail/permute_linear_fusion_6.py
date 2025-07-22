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
        self.linear2 = torch.nn.Linear(2, 2)
        self.linear3 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        v4 = v2.reshape((1, 2))
        v5 = torch.nn.functional.linear(v4, self.linear2.weight, self.linear2.bias)
        v8 = v5.unsqueeze(dim=1)
        v3 = (v8 + v2)
        v3 = v3.contiguous()
        v3 = torch.max(v3, dim=(- 1))[0]
        v4 = v3.unsqueeze(dim=(- 1))
        v3 = (v3 + v4.to(v3.dtype))
        v4 = (v3 == (- 1)).to(v3.dtype)
        v4 = torch.nn.functional.linear(v4, self.linear3.weight, self.linear3.bias)
        v4 = torch.sum(v4)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 2]' is invalid for input of size 4

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), (1, 2)), **{}):
shape '[1, 2]' is invalid for input of size 4

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''