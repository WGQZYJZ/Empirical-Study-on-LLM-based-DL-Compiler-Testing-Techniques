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
        self.lin = torch.nn.Linear(300, 400, bias=False)
        self.other = torch.randn(400, 600)

    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = (v1 + self.other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 300)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (400) must match the size of tensor b (600) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 400)), FakeTensor(..., device='cuda:0', size=(400, 600))), **{}):
Attempting to broadcast a dimension of length 600 at -1! Mismatching argument at index 1 had torch.Size([400, 600]); but expected shape should be broadcastable to [1, 400]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''