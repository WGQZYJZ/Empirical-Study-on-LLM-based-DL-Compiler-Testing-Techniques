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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        x2 = torch.nn.functional.relu(v1)
        v2 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        v2 = torch.sigmoid(v2)
        v3 = torch.max(v2, dim=(- 1))[0].sum()
        v3 = (v3 + v3)
        v3 = torch.max(v2, dim=(- 1))[0]
        v3 = (v3 + torch.max(v2, dim=(- 1))[1])
        x3 = (v3 + x2)
        v3 = x1.view(1, 4)
        y = (x3 - v3)
        return y




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([1, 4]); but expected shape should be broadcastable to [1, 2, 2]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''