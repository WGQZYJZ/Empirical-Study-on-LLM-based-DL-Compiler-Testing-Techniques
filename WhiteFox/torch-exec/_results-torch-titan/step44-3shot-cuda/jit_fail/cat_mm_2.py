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

    def forward(self, x1, x2):
        v = ([torch.mm(x1, x2) for _ in range(2)] + list(range(5)))
        return torch.cat(v, 0)




func = Model().to('cuda')



x1 = torch.randn(4, 4)



x2 = torch.randn(4, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
expected Tensor as element 2 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7561d66699e0>(*([FakeTensor(..., device='cuda:0', size=(4, 4)), FakeTensor(..., device='cuda:0', size=(4, 4)), 0, 1, 2, 3, 4], 0), **{}):
expected Tensor as element 2 in argument 0, but got int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''