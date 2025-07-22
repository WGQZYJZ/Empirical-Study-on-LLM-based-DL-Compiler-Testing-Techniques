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

    def forward(self, x):
        t1 = F.conv2d(x, 3, 8, 1, stride=1, padding=1, bias=None)
        t2 = (t1 + other)
        t3 = F.relu(t2)
        return t3




func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, int, int, int, bias=NoneType, padding=int, stride=int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the keywords were incorrect: bias, stride
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the keywords were incorrect: bias, stride


jit:
Failed running call_function <built-in method conv2d of type object at 0x7685224699e0>(*(1, 3, 8, 1), **{'stride': 1, 'padding': 1, 'bias': None}):
conv2d() received an invalid combination of arguments - got (int, int, int, int, bias=NoneType, padding=int, stride=int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the keywords were incorrect: bias, stride
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the keywords were incorrect: bias, stride


from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''