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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)
        self.linear3 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 3, 1)
        v3 = torch.nn.functional.linear(x1, self.linear2.weight, self.linear2.bias)
        v4 = v3.permute(0, 3, 2, 1)
        v5 = torch.nn.functional.linear(v2, self.linear3.weight, self.linear3.bias)
        return torch.nn.functional.linear((v1 + v4), v5, self.linear3.bias)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
t() expects a tensor with <= 2 dimensions, but self is 4D

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(2,), requires_grad=True))), **{}):
t() expects a tensor with <= 2 dimensions, but self is 4D

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''