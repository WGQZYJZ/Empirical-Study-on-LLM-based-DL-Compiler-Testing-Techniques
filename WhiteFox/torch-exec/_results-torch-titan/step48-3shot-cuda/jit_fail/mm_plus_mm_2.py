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

    def forward(self, input):
        matrix = torch.nn.Parameter(torch.randn(1024, 1000))
        output = torch.mm(input, matrix)
        return output




func = Model().to('cuda')



input = torch.randn(5, 15)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x78625e6699e0>(*(FakeTensor(..., device='cuda:0', size=(5, 15)), Parameter(FakeTensor(..., size=(1024, 1000), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [5, 15] X [1024, 1000].

from user code:
   File "<string>", line 19, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''