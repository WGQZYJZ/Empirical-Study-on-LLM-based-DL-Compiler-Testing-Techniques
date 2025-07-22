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
        self.linear = torch.nn.Linear(1, 8, bias=True)
        self.clamp = torch.nn.Threshold

    def forward(self, inputs):
        intermediate = self.linear(inputs)
        output = self.clamp(intermediate, 0, 6)
        output = (output / 6)
        return output



func = Model().to('cuda')



inputs = torch.randn(1, 1)


test_inputs = [inputs]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for /: 'Threshold' and 'int'

jit:
'NoneType' object has no attribute '__code__'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''