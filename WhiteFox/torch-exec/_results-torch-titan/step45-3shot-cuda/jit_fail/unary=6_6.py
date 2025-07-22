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



class Model_2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv3d = torch.nn.Conv3d(3, 3, kernel_size=3, padding=[2, 1, 1], bias=True)
        self.relu = torch.nn.ReLU(inplace=True)
        self.maxpool3d = torch.nn.MaxPool3d(kernel_size=2, padding=0, stride=1, dilation=1, ceil_mode=False)
        self.sigmoid = torch.nn.Sigmoid()
        self.dropout = torch.nn.Dropout3d(p=0)

    def forward(self, x1):
        v1 = self.conv3d(x1)
        v2 = self.relu(v1)
        v3 = torch.max(v2, dim=2, keepdim=True)
        v4 = torch.mean(v3, dim=2, keepdim=True)
        v5 = self.sigmoid(v4)
        v6 = self.dropout(v5)
        return v6




func = Model_2().to('cuda')



x1 = torch.randn(1, 3, 64, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mean() received an invalid combination of arguments - got (torch.return_types.max, keepdim=bool, dim=int), but expected one of:
 * (Tensor input, *, torch.dtype dtype)
      didn't match because some of the keywords were incorrect: keepdim, dim
 * (Tensor input, tuple of ints dim, bool keepdim, *, torch.dtype dtype, Tensor out)
 * (Tensor input, tuple of names dim, bool keepdim, *, torch.dtype dtype, Tensor out)


jit:
Failed running call_function <built-in method mean of type object at 0x7f0c374699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 3, 1, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 3, 1, 64, 64), dtype=torch.int64)),), **{'dim': 2, 'keepdim': True}):
mean() received an invalid combination of arguments - got (tuple, keepdim=bool, dim=int), but expected one of:
 * (Tensor input, *, torch.dtype dtype)
      didn't match because some of the keywords were incorrect: keepdim, dim
 * (Tensor input, tuple of ints dim, bool keepdim, *, torch.dtype dtype, Tensor out)
 * (Tensor input, tuple of names dim, bool keepdim, *, torch.dtype dtype, Tensor out)


from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''