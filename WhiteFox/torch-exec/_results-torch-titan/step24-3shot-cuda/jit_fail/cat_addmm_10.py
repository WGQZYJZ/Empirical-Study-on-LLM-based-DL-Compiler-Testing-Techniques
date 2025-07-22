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
        self.layers_2 = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        x = x.expand([3, 3])
        x = self.layers_2(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The expanded size of the tensor (3) must match the existing size (2) at non-singleton dimension 1.  Target sizes: [3, 3].  Tensor sizes: [2, 2]

jit:
Failed running call_method expand(*(FakeTensor(..., device='cuda:0', size=(2, 2)), [3, 3]), **{}):
expand: attempting to expand a dimension of length 2!

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''