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
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        x = x.flatten(start_dim=1)
        y = torch.stack([x, x, x], dim=1)
        x = x.flatten(start_dim=1)
        return torch.cat([x, y], dim=1)




func = Model().to('cuda')



x = torch.randn(1, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''