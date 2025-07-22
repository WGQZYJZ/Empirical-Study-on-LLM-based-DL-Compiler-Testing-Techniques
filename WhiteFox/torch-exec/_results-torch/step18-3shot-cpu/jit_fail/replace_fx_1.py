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

class MyModel(torch.nn.Module):

    def __init__(self, dim=32):
        super(MyModel, self).__init__()
        self.proj = torch.nn.Linear(30, dim)

    def forward(self, z):
        t1 = torch.rand_like(z)
        t2 = torch.nn.functional.dropout(t1, p=0.2)
        t3 = torch.rand_like(z)
        return t3 + t2 + self.proj(t3)



func = MyModel().to('cpu')


z1 = torch.zeros([1, 30])

test_inputs = [z1]

# JIT_FAIL
'''
direct:
The size of tensor a (30) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 30)), FakeTensor(..., size=(1, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 32]); but expected shape should be broadcastable to [1, 30]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''