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
        self.linear_1 = torch.nn.Linear(2, 4)
        self.linear_2 = torch.nn.Linear(2, 2)

    def forward(self, x3):
        v0 = x3
        v1 = torch.nn.functional.linear(v0, self.linear_1.weight, self.linear_1.bias)
        v2 = v1.permute(0, 2, 1)
        return torch.nn.functional.linear(v2, self.linear_2.weight, self.linear_2.bias)




func = Model().to('cuda')



x3 = torch.randn(1, 2, 2)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
KeyError: 'example_value'


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''