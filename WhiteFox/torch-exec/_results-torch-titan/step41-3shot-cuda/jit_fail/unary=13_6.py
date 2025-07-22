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
        self.linear = torch.nn.Linear(12, 8)

    def forward(self, x1):
        v5 = torch.add(x1, x1)
        v1 = self.linear(v5)
        v2 = torch.sigmoid(v1)
        v3 = torch.mm(v5, v5.t())
        v4 = (v3 * v2)
        return v4



func = Model().to('cuda')



x1 = torch.randn(5, 12)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(5, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([5, 8]); but expected shape should be broadcastable to [5, 5]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''