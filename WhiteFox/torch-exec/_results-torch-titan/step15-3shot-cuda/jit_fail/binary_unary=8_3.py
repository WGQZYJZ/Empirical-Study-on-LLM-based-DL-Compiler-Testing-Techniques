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

    def forward(self, x1):
        v1 = torch.relu(x1)
        v2 = torch.dropout(v1, (1 - 0.3))
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 8, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout() missing 1 required positional arguments: "train"

jit:
Failed running call_function <built-in method dropout of type object at 0x7d4cb78699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 128, 128)), 0.7), **{}):
dropout() missing 1 required positional arguments: "train"

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''