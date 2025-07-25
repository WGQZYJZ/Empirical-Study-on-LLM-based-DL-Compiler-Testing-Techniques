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

    def forward(self, x):
        v = torch.bmm(x.unsqueeze(0), torch.ones(2, 2, 2))
        return v



func = Model().to('cuda')



x = torch.randn(2, 2, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

jit:
Failed running call_function <built-in method bmm of type object at 0x71fc58e699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 1)), FakeTensor(..., size=(2, 2, 2))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''