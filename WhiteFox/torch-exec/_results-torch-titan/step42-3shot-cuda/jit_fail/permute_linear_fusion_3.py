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
        self.conv = torch.nn.Conv2d(2, 1, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1, 3)
        v2 = torch.nn.functional.conv2d(v1, self.conv.weight, None, [1, 1], [1, 0], [1, 0], 1, False)
        v2 = torch.nn.functional.hardtanh(v1, (- 1), 6)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Parameter, NoneType, list, list, list, int, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


jit:
Failed running call_function <built-in method conv2d of type object at 0x78aba30699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2), requires_grad=True)), None, [1, 1], [1, 0], [1, 0], 1, False), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, NoneType, immutable_list, immutable_list, immutable_list, int, bool), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''