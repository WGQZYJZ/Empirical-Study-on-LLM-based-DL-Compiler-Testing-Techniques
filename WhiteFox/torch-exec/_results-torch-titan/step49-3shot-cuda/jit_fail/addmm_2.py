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
        v1 = torch.mv(x1, x2)
        v2 = (v1 + inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3, requires_grad=True)



x2 = torch.randn(3, 3, requires_grad=True)



inp = torch.randn(3)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
vector + matrix @ vector expected, got 1, 2, 2

jit:
Failed running call_function <built-in method mv of type object at 0x765eb14699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
matrix @ vector expected, got 2, 2

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''