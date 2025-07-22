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

    def forward(self, x1, x2, inp, inp2):
        v1 = torch.mm(inp2, (x2 + 323))
        v2 = (v1 - inp)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3)



inp2 = torch.randn(3, 3)

inp = 1

test_inputs = [x1, x2, inp2, inp]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7b030c2699e0>(*(1, FakeTensor(..., device='cuda:0', size=(3, 3))), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''