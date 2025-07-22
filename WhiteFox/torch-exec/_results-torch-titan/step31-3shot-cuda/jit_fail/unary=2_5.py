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
        self.conv_transpose = torch.nn.ConvTranspose2d(9, 9, 2, stride=2, padding=1, output_padding=1)

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), 1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 * 0.5)
        v4 = ((v2 * v2) * v2)
        v5 = (v4 * 0.044715)
        v6 = (v2 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = torch.cat((x2, v9), 1)
        v11 = (v3 * v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(2, 9, 10, 2)



x2 = torch.randn(7, 9, 14, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 2 but got size 7 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7199af4699e0>(*((FakeTensor(..., device='cuda:0', size=(2, 9, 10, 2)), FakeTensor(..., device='cuda:0', size=(7, 9, 14, 3))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 2 but got 7 for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''