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
        self.fc = torch.nn.Linear(4, 3)

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 + other
        return v2


func = Model().to('cpu')


x1 = torch.randn(4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (10) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3,)), FakeTensor(..., size=(10,))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([10]); but expected shape should be broadcastable to [3]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''