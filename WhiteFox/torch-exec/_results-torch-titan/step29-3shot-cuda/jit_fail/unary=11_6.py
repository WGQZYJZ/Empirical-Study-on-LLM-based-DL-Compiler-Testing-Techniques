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



class SubModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(5, 10, 3, stride=2, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(10, 10, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x1):
        v = self.conv_transpose1(x1)
        v = self.conv_transpose2(v)
        return v




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.sub_model = SubModel()

    def forward(self, x1):
        v = self.sub_model.conv_transpose(x1)
        return v




func = Model().to('cuda')



x1 = torch.randn(1, 5, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'SubModel' object has no attribute 'conv_transpose'

jit:
conv_transpose

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''