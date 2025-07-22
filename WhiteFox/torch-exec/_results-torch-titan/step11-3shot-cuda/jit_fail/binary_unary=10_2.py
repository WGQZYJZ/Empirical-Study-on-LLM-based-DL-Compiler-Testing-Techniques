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
        self.linear = torch.nn.Linear((28 * 28), 10)

    def forward(self, x1):
        v1 = self.linear(x1).view((- 1), (28 * 28))
        v2 = (v1 + torch.zeros(1, (28 * 28), device=x1.device))
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(10, (28 * 28))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 784]' is invalid for input of size 100

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(10, 10)), -1, 784), **{}):
shape '[-1, 784]' is invalid for input of size 100

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''