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

    def forward(self, x):
        y = torch.cat((x, x), dim=1).view(x.shape[0], (- 1))
        z = y.view(y.shape[0], (- 1))
        return z.add(torch.sin(x)).sigmoid()




func = Model().to('cuda')



x = torch.randn(2, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_method add(*(FakeTensor(..., device='cuda:0', size=(2, 8)), FakeTensor(..., device='cuda:0', size=(2, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([2, 2, 2]); but expected shape should be broadcastable to [1, 2, 8]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''