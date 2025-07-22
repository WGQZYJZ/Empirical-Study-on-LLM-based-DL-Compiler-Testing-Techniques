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
        self.linear = torch.nn.Linear(4, 2)

    def forward(self, x1):
        a = (torch.rand_like(x1) + torch.tensor([2], device=x1.device))
        x2 = (a * torch.nn.functional.dropout(self.linear(a)))
        a = torch.randn((), device=x1.device)
        return F.dropout(x2, p=0.5, training=False)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)), FakeTensor(..., device='cuda:0', size=(1, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 2, 2]); but expected shape should be broadcastable to [1, 2, 4]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''