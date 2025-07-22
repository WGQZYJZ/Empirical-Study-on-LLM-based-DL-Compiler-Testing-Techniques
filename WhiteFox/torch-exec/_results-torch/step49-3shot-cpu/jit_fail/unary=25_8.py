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

    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = torch.nn.Linear(8, 6)(x1)
        t2 = v1.flatten() > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(t2.to(dtype=x1.dtype), v1, v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
where expected condition to be a boolean tensor, but got a tensor with dtype Float

jit:
Failed running call_function <built-in method where of type object at 0x7150be596ec0>(*(FakeTensor(..., size=(6,)), FakeTensor(..., size=(1, 6)), FakeTensor(..., size=(1, 6))), **{}):
expected predicate to be bool, got torch.float32

from user code:
   File "<string>", line 23, in torch_dynamo_resume_in_forward_at_20


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''