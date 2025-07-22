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



class ReLU6(torch.autograd.Function):

    @staticmethod
    def forward(ctx, input):
        output = torch.clamp(input, min=0, max=6)
        ctx.save_for_backward(output)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        (output,) = ctx.saved_tensors
        grad_input = grad_output.masked_fill((output > 6), 0.0)
        grad_input = grad_input.masked_fill((output < 0), 0.0)
        return grad_input




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        b = torch.cat((x1, x2), 1)
        a = ReLU6.apply(b)
        c = a[:, 0:4096]
        return c



func = Model().to('cuda')



x1 = torch.randn(6, 4096, 10)



x2 = torch.randn(6, 4096, 20)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 10 but got size 20 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7bd102a699e0>(*((FakeTensor(..., device='cuda:0', size=(6, 4096, 10)), FakeTensor(..., device='cuda:0', size=(6, 4096, 20))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 10 but got 20 for tensor number 1 in the list

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''