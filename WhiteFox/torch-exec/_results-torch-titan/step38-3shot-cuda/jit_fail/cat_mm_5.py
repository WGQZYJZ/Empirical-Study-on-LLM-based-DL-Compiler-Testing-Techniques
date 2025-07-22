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
        v1 = torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 1)
        return torch.cat([torch.mm(v1, torch.rand(1, 1)), torch.mm(x1, torch.cat([x1, x2], 1)), torch.mm(v1, torch.rand(1, 1)), torch.mm(x1, torch.cat([x2, x2], 1)), torch.mm(v1, torch.rand(1, 1), 1), torch.mm(x1, torch.cat([x2, x2], 1))], 1)




func = Model().to('cuda')



x1 = torch.randn(2, 1)



x2 = torch.randn(1, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x7943682699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., size=(1, 1))), **{}):
a and b must have same reduction dim, but got [2, 4] X [1, 1].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''