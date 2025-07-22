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

    def forward(self, x1, x2, x3):
        v1 = torch.reshape(x1, (3, 2, 1))
        v2 = torch.reshape(x2, (3, 2, 1))
        v3 = torch.bmm(v1, v2)
        v4 = torch.bmm(v3, v2)
        v5 = torch.bmm(v3, v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 6)

x2 = torch.randn(1, 6)

x3 = torch.randn(1, 6)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 1] but got: [3, 2].

jit:
Failed running call_function <built-in method bmm of type object at 0x7e0456b96ec0>(*(FakeTensor(..., size=(3, 2, 1)), FakeTensor(..., size=(3, 2, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 1] but got: [3, 2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''