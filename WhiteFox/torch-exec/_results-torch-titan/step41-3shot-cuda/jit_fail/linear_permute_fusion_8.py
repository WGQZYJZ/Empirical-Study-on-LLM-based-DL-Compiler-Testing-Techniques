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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        return torch.Tensor.permute(v1, 0, 1)




func = Model().to('cuda')




x1 = torch.randn(5, 2, 2, device='cpu', dtype=torch.float16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 must have the same dtype, but got Half and Float

jit:
Failed running call_function <method 'permute' of 'torch._C._TensorBase' objects>(*(FakeTensor(..., device='cuda:0', size=(5, 2, 2)), 0, 1), **{}):
Attempting to permute a tensor of rank 3, but received a permutation of length 2!

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''