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

    def forward(self, x, y, z):
        if (x is None):
            pass
        return torch.add(y, z)




func = Model().to('cuda')



x = torch.randn(1, 3, 4)



y = torch.randn(1, 5, 6)


y = torch.randn(1, 5, 6)


x = torch.randn(1, 3, 4)



z = torch.randn(x.shape[0], y.shape[1])


test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (5) at non-singleton dimension 2

jit:
Failed running call_function <built-in method add of type object at 0x7a1dc30699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 6)), FakeTensor(..., device='cuda:0', size=(1, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -1! Mismatching argument at index 1 had torch.Size([1, 5]); but expected shape should be broadcastable to [1, 5, 6]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''