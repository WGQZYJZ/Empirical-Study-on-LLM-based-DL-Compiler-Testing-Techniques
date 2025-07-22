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
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = (x1 + self.linear.weight)
        x1 = self.linear(v1)
        v2 = torch.abs(x1)
        return (v1 * v2)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 2), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 3 at -2! Mismatching argument at index 1 had torch.Size([3, 2]); but expected shape should be broadcastable to [1, 2, 2]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''