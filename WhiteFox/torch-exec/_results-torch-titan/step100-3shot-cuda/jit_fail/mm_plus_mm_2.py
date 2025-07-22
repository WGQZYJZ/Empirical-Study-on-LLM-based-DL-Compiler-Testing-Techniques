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

    def forward(self, a, b, c, d, e):
        g1 = torch.mm(a, b)
        g2 = torch.mm(e, e)
        g = (g1 + g2)
        g3 = torch.mm(d, e)
        g4 = torch.mm(d, e)
        return ((g + g3) + g4)




func = Model().to('cuda')



a = torch.randn(2, 2, requires_grad=True)



b = torch.randn(2, 2, requires_grad=True)



c = torch.randn(4, 2, requires_grad=True)



d = torch.randn(4, 2, requires_grad=True)

e = 1

test_inputs = [a, b, c, d, e]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7eb8900699e0>(*(1, 1), **{}):
mm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''