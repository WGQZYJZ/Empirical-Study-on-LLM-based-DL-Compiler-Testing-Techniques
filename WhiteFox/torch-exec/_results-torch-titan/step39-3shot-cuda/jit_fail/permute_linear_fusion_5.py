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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        x2 = x1.detach()
        x3 = x2.permute(0, 2, 1)
        y2 = torch.nn.functional.linear(x3, self.linear.weight, self.linear.bias)
        x2 = torch.max(y2, dim=1)[1].unsqueeze(dim=1)
        y2 = torch.nn.functional.linear(y2, self.linear.weight, self.linear.bias)
        x2 = torch.max(y2, dim=1)[1].unsqueeze(dim=1)
        return torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 must have the same dtype, but got Long and Float

jit:
backend='inductor' raised:
KeyError: 'example_value'


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''