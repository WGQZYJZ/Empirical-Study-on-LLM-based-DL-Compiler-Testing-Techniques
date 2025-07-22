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
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, input):
        return (self.linear(input) + None)



func = Model().to('cuda')



x = torch.randn(3, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for +: 'Tensor' and 'NoneType'

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 10)), None), **{}):
unsupported operand type(s) for +: 'FakeTensor' and 'NoneType'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''