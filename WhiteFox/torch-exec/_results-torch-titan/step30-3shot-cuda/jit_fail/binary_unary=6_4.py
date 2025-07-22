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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1):
        y1 = self.linear(x1)
        z1 = torch.rand(1, 4)
        k1 = (z1 + y1)
        y2 = torch.cat((k1, y1), dim=1)
        y3 = torch.reshape(y2, (1, 16))
        y4 = torch.transpose(y3, 1, 2)
        y5 = torch.flatten(y4, start_dim=1)
        y6 = self.linear(y5)
        y7 = self.linear(y6)
        return y7



func = Model().to('cuda')



x1 = torch.randn(2, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 4)), FakeTensor(..., device='cuda:0', size=(2, 8))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([2, 8]); but expected shape should be broadcastable to [1, 4]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''