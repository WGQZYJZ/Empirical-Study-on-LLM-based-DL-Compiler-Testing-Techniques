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
        self.conv2d = torch.nn.Conv2d(3, 5, 1, stride=2)
        self.avg_pool2d = torch.nn.AvgPool2d(kernel_size=2)

    def forward(self, x0):
        v0 = self.conv2d(x0)
        v1 = torch.relu(v0)
        v2 = self.avg_pool2d(v1)
        v3 = v2.view((1, (- 1)))
        v4 = torch.softmax(v3)
        v5 = v4.mm(torch.Tensor([[5.18, (- 18.76), 13.96, 32.95, 43.09, (- 29.25), (- 45.07), (- 12.6), (- 23.83), 8.78, 53.87, 38.49, 96.3, 44.88, (- 66.93), (- 67.88), (- 51.33)]]))
        return v5




func = Model().to('cuda')



x0 = torch.randn(1, 3, 10, 10)


test_inputs = [x0]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


jit:
Failed running call_function <built-in method softmax of type object at 0x71d6004699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 20)),), **{}):
softmax() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype, *, Tensor out)
 * (Tensor input, name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''