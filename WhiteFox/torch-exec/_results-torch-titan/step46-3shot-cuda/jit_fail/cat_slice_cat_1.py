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

    def forward(self, x1, x2, x3):
        v1 = torch.cat(x1, x2, x3)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:1]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 1, 240, 480)



x2 = torch.randn(1, 1, 480, 240)



x3 = torch.randn(1, 1, 240, 480)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor, Tensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x7439fb4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 240, 480)), FakeTensor(..., device='cuda:0', size=(1, 1, 480, 240)), FakeTensor(..., device='cuda:0', size=(1, 1, 240, 480))), **{}):
cat() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''