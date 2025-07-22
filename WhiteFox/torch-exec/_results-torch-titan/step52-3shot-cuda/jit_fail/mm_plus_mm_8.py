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

    def forward(self, input1, input2, input3):
        t1 = torch.mm(input1, input4)
        t2 = torch.mm(input2, input4)
        t3 = torch.mm(input3, input4)
        t4 = ((t1 + t2) + t3)
        return t4




func = Model().to('cuda')



input1 = torch.randn(2, 2)



input2 = torch.randn(2, 2)



input3 = torch.randn(2, 2)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x77e77ec699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., size=(8, 8))), **{}):
a and b must have same reduction dim, but got [2, 2] X [8, 8].

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''