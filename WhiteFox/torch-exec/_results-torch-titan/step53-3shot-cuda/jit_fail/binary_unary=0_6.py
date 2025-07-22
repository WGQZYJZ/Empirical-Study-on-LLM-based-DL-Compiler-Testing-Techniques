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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 3, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 + x)
        v3 = torch.softmax(v2)
        v4 = self.conv2(v3)
        v5 = (v4 + v1)
        v6 = torch.relu(v5)
        return v6




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method softmax of type object at 0x7673ea6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{}):
softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''