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

    def forward(self, x1, x2, p1):
        v1 = torch.mm(x1, x2)
        v2 = (v1 + x1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1564, 3676)



x2 = torch.randn(3676, 32)

p1 = 1

test_inputs = [x1, x2, p1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (3676) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1564, 32)), FakeTensor(..., device='cuda:0', size=(1564, 3676))), **{}):
Attempting to broadcast a dimension of length 3676 at -1! Mismatching argument at index 1 had torch.Size([1564, 3676]); but expected shape should be broadcastable to [1564, 32]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''