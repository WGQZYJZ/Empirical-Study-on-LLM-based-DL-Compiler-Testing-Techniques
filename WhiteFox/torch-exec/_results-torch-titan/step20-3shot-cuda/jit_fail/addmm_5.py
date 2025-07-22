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
        x1 = torch.t(x1)
        v1 = torch.bmm(x1, x2)
        v2 = v1
        v2 = (v2 + inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 5, 5)

inp = 1

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7b030c2699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 5, 5))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''