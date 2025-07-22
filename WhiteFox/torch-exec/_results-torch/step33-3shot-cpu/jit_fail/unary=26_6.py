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
        self.conv_t = torch.nn.ConvTranspose2d(2, 5, 5, stride=1)

    def forward(self, x):
        x = self.conv_t(x)
        x1 = x + torch.nn.functional.adaptive_avg_pool2d(x * 0.303, (1, 1))
        x2 = x1 > 1
        x4 = torch.where(x2, x, x1)
        x5 = x4 > 1
        return torch.where(x5 & ~x2 ^ x4, x4, x5)



func = Model().to('cpu')


x = torch.randn(5, 2, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
"bitwise_xor_cpu" not implemented for 'Float'

jit:
Failed running call_function <built-in method where of type object at 0x7c8fa4796ec0>(*(FakeTensor(..., size=(s0, 5, s2 + 4, s3 + 4)), FakeTensor(..., size=(s0, 5, s2 + 4, s3 + 4)), FakeTensor(..., size=(s0, 5, s2 + 4, s3 + 4), dtype=torch.bool)), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''