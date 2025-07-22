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
        self.conv = nn.ConvTranspose2d(1, 3, 3, stride=1, padding=0, output_padding=0, groups=1, bias=False)

    def forward(self, x):
        x = self.conv(x)
        x = x > 0
        x = x * -0.00900974227687354
        x = torch.where(x, x, x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 1, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x78e81fd96ec0>(*(FakeTensor(..., size=(s0, 3, s1 + 2, s2 + 2)), FakeTensor(..., size=(s0, 3, s1 + 2, s2 + 2)), FakeTensor(..., size=(s0, 3, s1 + 2, s2 + 2))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''