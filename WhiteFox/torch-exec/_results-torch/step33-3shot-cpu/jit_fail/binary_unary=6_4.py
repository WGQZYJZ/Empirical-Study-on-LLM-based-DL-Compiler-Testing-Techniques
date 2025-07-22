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
        self.linear = torch.nn.Linear(2, 16)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - [[5.0], [10.0]]
        v3 = torch.nn.functional.relu(v2)
        return v3


func = Model().to('cpu')



x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)

test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'Tensor' and 'list'

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(2, 16)), [[5.0], [10.0]]), **{}):
unsupported operand type(s) for -: 'FakeTensor' and 'immutable_list'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''