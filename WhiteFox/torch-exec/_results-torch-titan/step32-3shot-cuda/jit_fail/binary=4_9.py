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
        self.linear1 = torch.nn.Linear(3, 4)
        self.linear2 = torch.nn.Linear(3, 6)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(x)
        v3 = (v1 + v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4)), FakeTensor(..., device='cuda:0', size=(1, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -1! Mismatching argument at index 1 had torch.Size([1, 6]); but expected shape should be broadcastable to [1, 4]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''