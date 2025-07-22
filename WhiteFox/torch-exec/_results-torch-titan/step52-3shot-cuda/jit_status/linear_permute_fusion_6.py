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
        self.linear = torch.nn.Linear(4, 4)
        self.linear2 = torch.nn.Linear(4, 4)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 4, device='cpu')


test_inputs = [x1]

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