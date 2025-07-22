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
        self.conv = torch.nn.Conv2d(3, 2, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = torch.reshape(v3, (1, 8, 32, 48))
        v5 = (v4 * v1)
        v6 = (v5 * 0.044715)
        v7 = (v1 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.sigmoid(v8)
        v10 = (v9 + 1)
        v11 = (v2 * v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 3, 5, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 8, 32, 48]' is invalid for input of size 30

jit:
Failed running call_function <built-in method reshape of type object at 0x759e6ce699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 5)), (1, 8, 32, 48)), **{}):
shape '[1, 8, 32, 48]' is invalid for input of size 30

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''