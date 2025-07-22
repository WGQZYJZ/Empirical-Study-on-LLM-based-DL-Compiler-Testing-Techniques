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

    def forward(self, inp, x1, x2):
        v1 = (inp * x1)
        t = torch.mm(x2, inp)
        t = (t * 1.2)
        v2 = (v1 + t)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 5)



x2 = torch.randn(5, 3)



inp = torch.randn(3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(3, 5)), FakeTensor(..., device='cuda:0', size=(5, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([5, 3]); but expected shape should be broadcastable to [3, 5]

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''