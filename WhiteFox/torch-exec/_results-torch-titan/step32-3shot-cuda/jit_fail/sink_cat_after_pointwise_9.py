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
        y = torch.cat(x, x, x)
        z = (y.view(x.shape[0], (- 1)).tanh() if (torch.numel(y) == torch.numel(x)) else y.view(x.shape[0], (- 1)).tanh())
        return z




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor, Tensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x70fa950699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3, 4)), FakeTensor(..., device='cuda:0', size=(2, 3, 4))), **{}):
cat() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''