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
        super(Model, self).__init__()

    def forward(self, x1, x2):
        out = torch.bmm(x1, torch.transpose(x2, 2, 1))
        mask = x1.sum(-1)
        weights = torch.softmax(mask, dim=-1)
        return torch.bmm(weights, out)


func = Model().to('cpu')


x1 = torch.randn(5, 16, 3, 16)

x2 = torch.randn(5, 3, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7aa6b3596ec0>(*(FakeTensor(..., size=(5, 16, 3, 16)), FakeTensor(..., size=(5, 16, 3, 16))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''