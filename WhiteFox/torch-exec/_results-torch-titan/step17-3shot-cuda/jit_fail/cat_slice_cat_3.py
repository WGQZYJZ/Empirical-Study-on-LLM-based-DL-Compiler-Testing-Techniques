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

    def forward(self, x1, x2):
        torch.cat(input=[x1, x2])
        return slice



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(3, 3, 128, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat() missing 1 required positional arguments: "tensors"

jit:
Failed running call_function <built-in method cat of type object at 0x75e02f4699e0>(*(), **{'input': [FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(3, 3, 128, 128))]}):
cat() missing 1 required positional arguments: "tensors"

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''