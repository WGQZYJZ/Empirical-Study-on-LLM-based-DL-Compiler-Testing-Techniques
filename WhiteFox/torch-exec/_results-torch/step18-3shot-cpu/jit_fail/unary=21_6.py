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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))
        self.tanh_1 = torch.nn.Tanh()

    def forward(self, x):
        x1 = self.conv_1(x)
        x2 = torch.tanh_1(x1)
        return x2



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 3, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'tanh_1'

jit:
AttributeError: module 'torch' has no attribute 'tanh_1'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''