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

    def forward(self, x):
        t1 = torch.randint(0, 10, size=[1])
        t2 = torch.nn.functional.dropout(x, 0.2, False)
        t3 = torch.rand_like(t2)
        t3 = torch.nn.functional.dropout(x, t2[0], True)
        t5 = t1 + t2[0]
        return x * t2



func = Model().to('cpu')


x = torch.randn((2, 2))

test_inputs = [x]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x74a92f7a5b80>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(2,)), True), **{}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''