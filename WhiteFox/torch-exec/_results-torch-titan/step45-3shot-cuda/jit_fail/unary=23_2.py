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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 1, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = x1.transpose(dim0=0, dim1=2)
        v2 = self.conv_transpose(v1)
        v3 = v2.transpose(dim0=0, dim1=2)
        v4 = torch.einsum('n i c h w, m c h w -> n m i', (v3, x2))
        v5 = torch.bmm(x2, torch.einsum('n c h w, c h w -> n c h w', (v3, v3)))
        return (v4, v5)




func = Model().to('cuda')



x1 = torch.randn(8, 1, 8, 8)



x2 = torch.randn(8, 1, 8, 8)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
einsum(): the number of subscripts in the equation (5) does not match the number of dimensions (4) for operand 0 and no ellipsis was given

jit:
Failed running call_function <function einsum at 0x79452edb0160>(*('n i c h w, m c h w -> n m i', (FakeTensor(..., device='cuda:0', size=(8, 3, 8, 8)), FakeTensor(..., device='cuda:0', size=(8, 1, 8, 8)))), **{}):
einsum(): the number of subscripts in the equation (5) does not match the number of dimensions (4) for operand 0 and no ellipsis was given

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''