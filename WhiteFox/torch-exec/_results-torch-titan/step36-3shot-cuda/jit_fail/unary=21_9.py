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
        super(ModelTanh, self).__init__()
        self.conv2d = nn.Conv2d(3, 32, 2)
        self.t5 = nn.Tensor = torch.empty([1, 1, 1, 1])

    def forward(self, x):
        v1 = self.conv2d(x)
        v1 = self.t5.tanh(v1)
        return v1




func = ModelTanh().to('cuda')



x = torch.randn(16, 3, 31, 31)


test_inputs = [x]

# JIT_FAIL
'''
direct:
tanh() takes no arguments (1 given)

jit:
Failed running call_method tanh(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)), FakeTensor(..., device='cuda:0', size=(16, 32, 30, 30))), **{}):
tanh() takes no arguments (1 given)

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''