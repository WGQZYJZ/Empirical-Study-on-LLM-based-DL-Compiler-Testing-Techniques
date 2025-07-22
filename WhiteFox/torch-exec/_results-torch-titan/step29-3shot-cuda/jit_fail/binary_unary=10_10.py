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
        self.linear = torch.nn.Linear(10, 5, bias=False)

    def forward(self, x1, x2):
        x_new = torch.cat([x1, x2], 1)
        v1 = self.linear(x_new)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7d7c04e699e0>(*([1, 1], 1), **{}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''