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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x1)
        v2 = torch.zeros(3, 3, 3)
        v3 = torch.addcmul(v2, v1, inp, value=1.0)
        v4 = v3.mean()
        return v4




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3, requires_grad=True)



inp = torch.randn(3, 3, 3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in method addcmul of type object at 0x7aecbd4699e0>(*(FakeTensor(..., size=(3, 3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3, 3))), **{'value': 1.0}):
Unhandled FakeTensor Device Propagation for aten.addcmul.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''