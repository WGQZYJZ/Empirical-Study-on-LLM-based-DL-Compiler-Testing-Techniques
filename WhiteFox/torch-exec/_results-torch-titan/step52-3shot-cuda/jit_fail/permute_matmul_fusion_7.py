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
        v1 = torch.randn(2, 2)
        v2 = torch.randn(2, 2)
        v3 = torch.randn(2, 2)
        v4 = torch.randn(2, 2)
        v5 = torch.randn(2, 2)
        v6 = torch.randn(2, 2)
        v7 = torch.bmm(v1, v3)
        v8 = torch.bmm(v2, v4)
        v9 = torch.bmm(v5, v7)
        v10 = torch.bmm(v6, v8)
        return torch.bmm(v9, v10)




func = Model().to('cuda')



x1 = torch.randn(2, 2, 2)



x2 = torch.randn(2, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7d5b0ba699e0>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2, 2))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''