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
        y1 = torch.cat((x, x), dim=1).view((- 1), 2)
        x1 = y1[:, :2]
        x2 = y1[:, 2:]
        x = (x1.tanh() + x2.sigmoid())
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (0) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(24, 2)), FakeTensor(..., device='cuda:0', size=(24, 0))), **{}):
Attempting to broadcast a dimension of length 0 at -1! Mismatching argument at index 1 had torch.Size([24, 0]); but expected shape should be broadcastable to [24, 2]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''