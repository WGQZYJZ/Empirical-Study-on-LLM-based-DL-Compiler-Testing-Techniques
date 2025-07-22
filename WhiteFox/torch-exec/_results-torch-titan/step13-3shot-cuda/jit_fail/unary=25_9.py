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
        self.linear = torch.nn.Linear(40, 60)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = (0.1 * v1)
        v4 = v1
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 40)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x7ef3a92699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 60)), FakeTensor(..., device='cuda:0', size=(1, 60)), FakeTensor(..., device='cuda:0', size=(1, 60))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''