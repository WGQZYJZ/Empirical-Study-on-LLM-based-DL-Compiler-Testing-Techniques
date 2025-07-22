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
        v1 = torch.mul(x1, x2)
        v2 = torch.cat(v1, 1)
        v3 = torch.cat([v2, v2, v2, v2], 1)
        return torch.mul(x1, v3)




func = Model().to('cuda')



x1 = torch.randn(2, 1)



x2 = torch.randn(1, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x707fef8699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4)), 1), **{}):
cat() received an invalid combination of arguments - got (FakeTensor, int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''