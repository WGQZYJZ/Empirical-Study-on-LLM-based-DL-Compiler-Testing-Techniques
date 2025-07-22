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

    def __init__(self, neg_value):
        super(Model, self).__init__()
        self.conv0 = torch.nn.ConvTranspose2d(32, 1, kernel_size=(3, 5), stride=(2, 3))
        self.conv = torch.nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.conv2 = torch.nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(1, 1))
        self.neg_value = neg_value

    def forward(self, x):
        x = self.conv(F.relu(self.conv2(self.conv0(x))))
        v0 = (self.neg_value * (self.conv_t.weight > 0))
        x = (x * v0)
        return x




neg_value = 0.1

func = Model(neg_value).to('cuda')



x = torch.randn(2, 32, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv_t'

jit:
conv_t

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''