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



class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        layer = nn.ConvTranspose2d(4, 3, kernel_size=3, stride=[1, 1], output_padding=[0, 0])
        self.sig = nn.Sigmoid()

    def forward(self, x):
        x1 = layer(x)
        x2 = self.sig(x1)
        return x2




func = Model().to('cuda')



x1 = torch.randn(1, 4, 12, 12, requires_grad=True)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'layer' is not defined

jit:
name 'layer' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''