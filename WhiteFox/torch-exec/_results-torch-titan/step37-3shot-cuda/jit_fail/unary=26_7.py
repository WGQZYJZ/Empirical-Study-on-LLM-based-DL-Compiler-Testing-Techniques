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



class block1(torch.nn.Module):

    def forward(self, input_tensor9):
        i4 = (input_tensor9 > (- 1.5216))
        i5 = (input_tensor9 * (- 0.5303))
        i6 = torch.where(i4, input_tensor9, i5)
        return torch.nn.functional.relu(i6)




class block2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(60, 92, 3, stride=1, padding=0, output_padding=0, bias=False)

    def forward(self, input_tensor9):
        i2 = input_tensor9.type(torch.float16)
        i3 = input_tensor9.size()
        i1 = self.conv_t(i2, bias=None)
        return block1()(i1)




class Model(torch.nn.Module):

    def forward(self, input_tensor2):
        b0 = block0(input_tensor2, weight=torch.randn(1, 1, 3, 3), bias=torch.randn(92))
        b2 = block2()(b0)
        return block1()(b2)




func = Model().to('cuda')



input_tensor2 = torch.randn(9, 60, 24, 21)


test_inputs = [input_tensor2]

# JIT_FAIL
'''
direct:
name 'block0' is not defined

jit:
name 'block0' is not defined

from user code:
   File "<string>", line 44, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''