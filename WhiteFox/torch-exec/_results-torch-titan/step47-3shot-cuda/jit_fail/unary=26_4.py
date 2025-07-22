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
        self.conv_t = torch.nn.ConvTranspose1d(52, 16, 8, stride=4, padding=2, bias=True)

    def forward(self, x22):
        z1 = self.conv_t(x22)
        z2 = (z1 > 0)
        z3 = (z1 * 0.353)
        z4 = torch.where(z2, z3, z1)
        return torch.max(z4, 0.546)




func = Model().to('cuda')



x22 = torch.randn(33, 52, 8)


test_inputs = [x22]

# JIT_FAIL
'''
direct:
max() received an invalid combination of arguments - got (Tensor, float), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


jit:
Failed running call_function <built-in method max of type object at 0x7f3a0d4699e0>(*(FakeTensor(..., device='cuda:0', size=(33, 16, 32)), 0.546), **{}):
max() received an invalid combination of arguments - got (FakeTensor, float), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''