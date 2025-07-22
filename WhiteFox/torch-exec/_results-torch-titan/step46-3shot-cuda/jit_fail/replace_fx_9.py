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

    def forward(self, x1):
        x2 = torch.rand_like(x1, dropout_p=0.1)
        x3 = F.interpolate(x1, x2, mode='nearest')
        x4 = F.dropout(x1, p=0.5)
        x5 = F.interpolate(x3, x4, mode='nearest')
        return x4




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x3 = F.interpolate(x1, scale_factor=x1.size()[(- 1)], mode='nearest')
        x2 = torch.rand_like(x3)
        x4 = F.interpolate(x1, x2, mode='nearest')
        return x4




func = Model().to('cuda')



x1 = torch.randn(1, 2, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
upsample_nearest2d() received an invalid combination of arguments - got (Tensor, list, NoneType), but expected one of:
 * (Tensor input, tuple of ints output_size, tuple of floats scale_factors)
      didn't match because some of the arguments have invalid types: (Tensor, !list of [Tensor, Tensor]!, !NoneType!)
 * (Tensor input, tuple of ints output_size, float scales_h, float scales_w, *, Tensor out)


jit:
Failed running call_function <function interpolate at 0x7c1bc58e1430>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4, 4)), FakeTensor(..., device='cuda:0', size=(1, 2, 16, 16))), **{'mode': 'nearest'}):
upsample_nearest2d() received an invalid combination of arguments - got (FakeTensor, list, NoneType), but expected one of:
 * (Tensor input, tuple of ints output_size, tuple of floats scale_factors)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !list of [FakeTensor, FakeTensor]!, !NoneType!)
 * (Tensor input, tuple of ints output_size, float scales_h, float scales_w, *, Tensor out)


from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''