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

    def forward(self, x1, x2, x3, x4):
        input1 = torch.nn.functional.conv_transpose3d(data=x1, weight=x2, bias=torch.ones(()), stride=x3, padding=x4)
        return input1




func = Model().to('cuda')



x1 = torch.randn(64, 20, 50, 100)



x2 = torch.randn(20, 16, 3, 3)



x3 = torch.randn(64)



x4 = torch.randn(6)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
conv_transpose3d() missing 2 required positional argument: "input", "weight"

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7bdf1ba699e0>(*(), **{'data': FakeTensor(..., device='cuda:0', size=(64, 20, 50, 100)), 'weight': FakeTensor(..., device='cuda:0', size=(20, 16, 3, 3)), 'bias': FakeTensor(..., size=()), 'stride': FakeTensor(..., device='cuda:0', size=(64,)), 'padding': FakeTensor(..., device='cuda:0', size=(6,))}):
conv_transpose3d() missing 2 required positional argument: "input", "weight"

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''