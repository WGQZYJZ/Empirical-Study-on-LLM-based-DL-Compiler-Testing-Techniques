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
        self.conv = torch.nn.Conv2d(2, 3, (5, 7), stride=(2, 1))

    def forward(self, x1, x2, other=1, padding1=None):
        x1 = F.conv2d(x1, self.conv.weight, self.conv.bias, (1, 1), (2, 0), (0, 0), (2, 1))
        x2 = self.conv(x2)
        x3 = ((x1 * 3) + (x2 / other))
        x3[:, :, 11:13, :] = (x3[:, :, 11:13, :] + padding1)
        return x3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)



x2 = torch.randn(1, 2, 100, 150)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Parameter, Parameter, tuple, tuple, tuple, tuple), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!)


jit:
Failed running call_function <built-in method conv2d of type object at 0x7f2bd5c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 64, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 2, 5, 7), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(3,), requires_grad=True)), (1, 1), (2, 0), (0, 0), (2, 1)), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor, tuple, tuple, tuple, tuple), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''