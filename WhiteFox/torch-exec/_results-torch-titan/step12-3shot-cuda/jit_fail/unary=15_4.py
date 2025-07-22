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

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, torch.randn(8, 3, 1, 1), None, [2, 2], 1, [1, 1], False)
        v2 = torch.nn.functional.prelu(v1, torch.randn(8))
        v3 = torch.relu(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Tensor, NoneType, list, int, list, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, Tensor, !NoneType!, !list of [int, int]!, !int!, !list of [int, int]!, !bool!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, Tensor, !NoneType!, !list of [int, int]!, !int!, !list of [int, int]!, !bool!)


jit:
Failed running call_function <built-in method conv2d of type object at 0x7edde58699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 256, 256)), FakeTensor(..., size=(8, 3, 1, 1)), None, [2, 2], 1, [1, 1], False), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, NoneType, immutable_list, int, immutable_list, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !NoneType!, !immutable_list of [int, int]!, !int!, !immutable_list of [int, int]!, !bool!)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !NoneType!, !immutable_list of [int, int]!, !int!, !immutable_list of [int, int]!, !bool!)


from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''