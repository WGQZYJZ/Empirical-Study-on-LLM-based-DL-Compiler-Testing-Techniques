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

    def forward(self, a, b, c, d, e, f):
        result = torch.mm(torch.mm(torch.mm(torch.mm(a, b), torch.mm(c, d)), e), f)
        result = (result + torch.mm(torch.mm(torch.mm(a, c), e), f))
        result = (result + torch.mm(torch.mm(a, c), torch.mm(d, f)))
        result = (result + torch.mm(torch.mm(a, e), torch.mm(d, f)))
        result = (result + torch.mm(torch.mm(e, b), torch.mm(d, f)))
        result = (result + torch.mm(e, torch.mm(d, f)))
        result = ((((result + a) + b) + c) + d)
        return result




func = Model().to('cuda')



a = torch.randn(3, 3)



b = torch.randn(3, 3)



c = torch.randn(3, 3)



d = torch.randn(3, 3)



f = torch.randn(3, 3)

e = 1

test_inputs = [a, b, c, d, f, e]

# JIT_FAIL
'''
direct:
mm(): argument 'mat2' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method mm of type object at 0x7faf32c699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 3)), 1), **{}):
mm(): argument 'mat2' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''