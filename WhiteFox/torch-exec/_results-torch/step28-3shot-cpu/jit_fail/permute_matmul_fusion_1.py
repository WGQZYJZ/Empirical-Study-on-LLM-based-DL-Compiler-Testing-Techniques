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

    def forward(self, x1, x2):
        v1 = x2.permute(1, 0, 2).unsqueeze_(2)
        v2 = torch.bmm(x1.permute(1, 2, 0), v1)
        v3 = v2.squeeze_()
        v4 = v3.transpose(1, 2)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

x2 = torch.randn(1, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch2 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7440c5b96ec0>(*(FakeTensor(..., size=(2, 2, 1)), FakeTensor(..., size=(2, 1, 1, 2))), **{}):
batch2 must be a 3D tensor

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''