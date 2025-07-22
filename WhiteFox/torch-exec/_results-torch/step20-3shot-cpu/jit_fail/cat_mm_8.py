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
        self.fc = torch.nn.Linear(15, 1)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        out = []
        v2 = torch.mm(x1, x2)
        for i in range(5):
            out.append(torch.cat((v1.unsqueeze(0), v2.unsqueeze(0)), dim=1))
            v2 = torch.mm(x1, v2)
        result = torch.stack(out)
        result = result.view(5, 2, 10)
        result = self.fc(result)
        return torch.cat([result, v2], dim=1)



func = Model().to('cpu')


x1 = torch.randn(4, 3)

x2 = torch.randn(3, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x3 and 4x5)

jit:
Failed running call_function <built-in method mm of type object at 0x72697cd96ec0>(*(FakeTensor(..., size=(4, 3)), FakeTensor(..., size=(4, 5))), **{}):
a and b must have same reduction dim, but got [4, 3] X [4, 5].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''