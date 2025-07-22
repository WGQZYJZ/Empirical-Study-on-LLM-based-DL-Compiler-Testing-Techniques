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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1, x2):
        o1 = self.linear(x1)
        o2 = (o1 + x2)
        o3 = o2.relu()
        return o3



func = Model().to('cuda')



x1 = torch.randn(1, 1, 3)



x2 = torch.randn(1, 1, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (3) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 8)), FakeTensor(..., device='cuda:0', size=(1, 1, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 3]); but expected shape should be broadcastable to [1, 1, 8]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''