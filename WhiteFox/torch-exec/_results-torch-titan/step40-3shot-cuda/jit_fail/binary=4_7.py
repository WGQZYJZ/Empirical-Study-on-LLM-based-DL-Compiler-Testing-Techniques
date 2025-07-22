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
        self.linear = torch.nn.Linear(3, 10)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + x)
        v3 = self.linear(v2)
        return v3



func = Model().to('cuda')



x = torch.randn(5, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(5, 10)), FakeTensor(..., device='cuda:0', size=(5, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([5, 3]); but expected shape should be broadcastable to [5, 10]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''