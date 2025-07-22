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
        self.conv_transpose = torch.nn.ConvTranspose2d(128, 5, 7, stride=1, padding=0)

    def forward(self, x1):
        v1 = torch.conv_transpose1d(x1, self.conv_transpose.weight, self.conv_transpose.bias, stride=1, padding=3, output_padding=2)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 128, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 4-dimensional input for 4-dimensional weight [128, 5, 7, 7], but got 3-dimensional input of size [1, 128, 10] instead

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7bd5580699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 128, 10)), Parameter(FakeTensor(..., device='cuda:0', size=(128, 5, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(5,), requires_grad=True))), **{'stride': 1, 'padding': 3, 'output_padding': 2}):
Expected 4-dimensional input for 4-dimensional weight [128, 5, 7, 7], but got 3-dimensional input of size [1, 128, 10] instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''