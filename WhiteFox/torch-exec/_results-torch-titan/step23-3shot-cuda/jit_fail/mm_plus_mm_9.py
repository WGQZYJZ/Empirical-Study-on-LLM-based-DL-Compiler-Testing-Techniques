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

    def forward(self, model_input):
        v1 = torch.mm(model_input, torch.rand(3, 7))
        v2 = torch.nn.functional.relu(v1)
        v3 = (v1 + v2)
        return v3




func = Model().to('cuda')



model_input = torch.randn(30, 30)


test_inputs = [model_input]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x74b8da6699e0>(*(FakeTensor(..., device='cuda:0', size=(30, 30)), FakeTensor(..., size=(3, 7))), **{}):
a and b must have same reduction dim, but got [30, 30] X [3, 7].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''