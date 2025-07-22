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
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - np.array([1, 0, 0])
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
operands could not be broadcast together with shapes (1,4) (3,) 

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, 4)), FakeTensor(..., size=(3,), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3]); but expected shape should be broadcastable to [1, 4]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''