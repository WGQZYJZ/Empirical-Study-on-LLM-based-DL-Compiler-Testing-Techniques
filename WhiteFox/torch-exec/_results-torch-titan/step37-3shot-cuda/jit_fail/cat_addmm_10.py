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
        super().__init__()
        self.layers = nn.Linear(3, 2)

    def forward(self, x):
        x = self.layers(x)
        z = torch.stack((x,), dim=1)
        y = torch.cat((z, x), dim=1)
        return y




func = Model().to('cuda')



x = torch.randn(2, 3)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''