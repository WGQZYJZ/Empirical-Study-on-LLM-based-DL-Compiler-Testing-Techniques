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
        v1 = torch.mm(inp, inp)
        v2 = v1.sum()
        v3 = v1.mean(dim=1, keepdim=True)
        v4 = v3.view(x1.size(0), (- 1))
        return torch.mm(v4, inp)




func = Model().to('cuda')



x1 = torch.randn(5, 5)



x2 = torch.randn(5, 5)



inp = torch.randn(5, 5)


test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x1 and 5x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7bc19ae699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 1)), FakeTensor(..., device='cuda:0', size=(5, 5))), **{}):
a and b must have same reduction dim, but got [5, 1] X [5, 5].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''