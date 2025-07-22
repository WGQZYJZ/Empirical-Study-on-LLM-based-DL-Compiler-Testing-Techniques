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
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1, x2=None):
        if (x2 is None):
            x2 = torch.empty(2, 3)
        v1 = self.linear(x1)
        v2 = (v1 + x2)
        return v2



func = Model().to('cuda')



x1 = torch.rand(3, 3)



x2 = torch.rand(2, 3, requires_grad=True)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([2, 3]); but expected shape should be broadcastable to [3, 4]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''