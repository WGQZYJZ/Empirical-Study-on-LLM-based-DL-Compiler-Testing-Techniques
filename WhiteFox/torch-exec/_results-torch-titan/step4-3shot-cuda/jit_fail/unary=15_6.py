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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = F.conv2d(x1, weight=self.conv.weight, bias=self.conv.bias, stride=1, padding=self.conv.padding, dilation=self.conv.dilation, groups=self.conv.in_channels, padding_mode=self.conv.padding_mode)
        v2 = torch.relu(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, padding_mode=str, groups=int, dilation=tuple, stride=int, padding=tuple, bias=Parameter, weight=Parameter), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


jit:
Failed running call_function <built-in method conv2d of type object at 0x735a704699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 256, 256)),), **{'weight': Parameter(FakeTensor(..., device='cuda:0', size=(8, 3, 1, 1), requires_grad=True)), 'bias': Parameter(FakeTensor(..., device='cuda:0', size=(8,), requires_grad=True)), 'stride': 1, 'padding': (1, 1), 'dilation': (1, 1), 'groups': 3, 'padding_mode': 'zeros'}):
conv2d() received an invalid combination of arguments - got (FakeTensor, padding_mode=str, groups=int, dilation=tuple, stride=int, padding=tuple, bias=FakeTensor, weight=FakeTensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''