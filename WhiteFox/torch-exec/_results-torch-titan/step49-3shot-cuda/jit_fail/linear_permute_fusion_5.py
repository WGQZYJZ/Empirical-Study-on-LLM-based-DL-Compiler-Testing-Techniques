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
        self.linear1 = torch.nn.Linear(3, 2)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v1, self.linear2.weight, self.linear2.bias)
        relu1 = torch.nn.functional.relu
        v4 = v3.view(x1.size(0), (- 1))
        (v5, v6) = relu1(v4)
        v7 = v5.view(1, (- 1))
        v8 = v5.unsqueeze((- 1))
        v9 = torch.sigmoid(v7)
        v10 = (v8 * v9)
        return v10




func = Model().to('cuda')



x0 = torch.randn(1, 2, 3)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 2, got 1)

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 6)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''