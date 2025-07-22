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

    def forward(self, x, y):
        x = torch.Tensor.addmm(b=x, mat1=y, mat2=y, alpha=1, beta=1)
        return x



func = Model().to('cuda')



x = torch.randn(8, 8)



y = torch.randn(8, 8)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
descriptor 'addmm' of 'torch._C._TensorBase' object needs an argument

jit:
Failed running call_function <method 'addmm' of 'torch._C._TensorBase' objects>(*(), **{'b': FakeTensor(..., device='cuda:0', size=(8, 8)), 'mat1': FakeTensor(..., device='cuda:0', size=(8, 8)), 'mat2': FakeTensor(..., device='cuda:0', size=(8, 8)), 'alpha': 1, 'beta': 1}):
descriptor 'addmm' of 'torch._C._TensorBase' object needs an argument

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''