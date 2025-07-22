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
        self.dropout = 0.1
        self.dim = 32

    def forward(self, query):
        output = torch.tanh(query)
        return output




func = Model().to('cuda')

query = 1

test_inputs = [query]

# JIT_FAIL
'''
direct:
tanh(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method tanh of type object at 0x7f3f604699e0>(*(1,), **{}):
tanh(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''