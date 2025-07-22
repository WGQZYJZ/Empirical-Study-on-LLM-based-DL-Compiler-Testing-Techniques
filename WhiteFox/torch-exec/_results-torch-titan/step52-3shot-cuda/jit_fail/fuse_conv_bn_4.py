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
        conv = torch.nn.Conv2d(1, 3, 3)
        self.conv = torch.nn.Sequential(conv, torch.nn.Conv2d(3, 3, 3))
        self.bn = torch.nn.BatchNorm2d(3)
        conv.register_backward_hook(self.backward_hook)

    def forward(self, x3):
        x = self.conv(x3)
        y = self.bn(x)
        z = self.conv(y)
        return z

    def backward_hook(self, module, grad_in, grad_out):
        print(grad_out[0].shape)




func = Model().to('cuda')



x3 = torch.randn(2, 1, 4, 4)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7fd9a2c699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 2, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(3, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 460, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 456, in _conv_forward
    return F.conv2d(input, weight, bias, self.stride,


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''