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
        super(Model, self).__init__()
        self.conv = torch.nn.Conv2d(4, 3, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return F.Sigmoid()(v1)



func = Model().to('cpu')


x1 = torch.randn(1, 4, 3, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'Sigmoid'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'Sigmoid'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''