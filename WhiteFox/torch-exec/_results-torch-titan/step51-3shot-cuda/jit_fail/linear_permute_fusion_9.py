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
        v12 = []
        v11 = []
        v4 = []
        v3 = x1
        v18 = self.linear(v3)
        v5 = v18.permute(0, 2, 1)
        v12.append(v5)
        v10 = torch.cat(v12, 0)
        v14 = torch.cat(v11, 0)
        v13 = torch.cat(v4, 0)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
torch.cat(): expected a non-empty list of Tensors

jit:
Failed running call_function <built-in method cat of type object at 0x7baa9f8699e0>(*([], 0), **{}):
cat expects at least one tensor, but received zero!

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''