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
        self.linear1 = torch.nn.Linear(20, 10)
        self.linear2 = torch.nn.Linear(10, 30)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = (v1 + x)
        v4 = self.linear2(relu(v2))
        return v4



func = Model().to('cuda')



x = torch.randn(1, 20)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 10)), FakeTensor(..., device='cuda:0', size=(1, 20))), **{}):
Attempting to broadcast a dimension of length 20 at -1! Mismatching argument at index 1 had torch.Size([1, 20]); but expected shape should be broadcastable to [1, 10]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''