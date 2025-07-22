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
        self.linear1 = torch.nn.Linear(3, 9)
        self.linear2 = torch.nn.Linear(9, 4)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 - torch.tensor([1.2, 2.3, 3.4, 4.5], dtype=torch.float32))
        return self.linear2(torch.relu(v2))



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (9) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 9)), FakeTensor(..., size=(4,))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4]); but expected shape should be broadcastable to [1, 9]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''