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
        x1 = torch.bmm(x1, x2)
        x1 = torch.nn.functional.relu(x1)
        return x1



func = Model().to('cpu')


x1 = torch.randn(4, 2, 3)

x2 = torch.randn(4, 2, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 3] but got: [4, 2].

jit:
Failed running call_function <built-in method bmm of type object at 0x7dea82396ec0>(*(FakeTensor(..., size=(s0, s3, s4)), FakeTensor(..., size=(s0, 2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s4] but got: [s0, 2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''