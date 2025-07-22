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



class Model2(torch.nn.Module):

    def __init__(self):
        super(Model2, self).__init__()

    def forward(self, x1, x2, x4):
        x1 = torch.nn.functional.conv2d(input, weight=x2, bias=x2, stride=x4, padding=x4, dilation=x1, groups=x1)
        return x1




func = Model2().to('cuda')



input = torch.randn(1, 3, 4, 4)



x2 = torch.randn(3, 3, 4, 4)

x1 = 1

test_inputs = [input, x2, x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, groups=Tensor, dilation=Tensor, stride=int, padding=int, bias=Tensor, weight=Tensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, weight=Tensor, bias=Tensor, !stride=int!, !padding=int!, !dilation=Tensor!, !groups=Tensor!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, weight=Tensor, bias=Tensor, !stride=int!, !padding=int!, !dilation=Tensor!, !groups=Tensor!)


jit:
Failed running call_function <built-in method conv2d of type object at 0x70f9266699e0>(*(FakeTensor(..., size=(1, 3, 4, 4)),), **{'weight': FakeTensor(..., device='cuda:0', size=(3, 3, 4, 4)), 'bias': FakeTensor(..., device='cuda:0', size=(3, 3, 4, 4)), 'stride': 1, 'padding': 1, 'dilation': FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)), 'groups': FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4))}):
conv2d() received an invalid combination of arguments - got (FakeTensor, groups=FakeTensor, dilation=FakeTensor, stride=int, padding=int, bias=FakeTensor, weight=FakeTensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !weight=FakeTensor!, !bias=FakeTensor!, !stride=int!, !padding=int!, !dilation=FakeTensor!, !groups=FakeTensor!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !weight=FakeTensor!, !bias=FakeTensor!, !stride=int!, !padding=int!, !dilation=FakeTensor!, !groups=FakeTensor!)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''