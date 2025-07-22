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
        self.linear = torch.nn.Linear(2, 2)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        z = self.linear.weight
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = self.sigmoid(v2)
        y = torch.rand(1, 2, 3, requires_grad=True)
        a = torch.nn.functional.conv1d(x2, y, None, 1, (0, 0), 1, 1, False, [], False)
        return a




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv1d() received an invalid combination of arguments - got (Tensor, Tensor, NoneType, int, tuple, int, int, bool, list, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


jit:
Failed running call_function <built-in method conv1d of type object at 0x79fb092699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1, 2, 3), requires_grad=True), None, 1, (0, 0), 1, 1, False, [], False), **{}):
conv1d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, NoneType, int, tuple, int, int, bool, immutable_list, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''