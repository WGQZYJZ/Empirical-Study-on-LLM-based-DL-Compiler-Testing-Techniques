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
        v1 = torch.cat(input_tensors=x, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:((v1.shape[1] - x.shape[1]) + 1)]
        return torch.cat([v1, v3], dim=1)



func = Model().to('cuda')



x1 = torch.randn(4, 8, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (dim=int, input_tensors=Tensor, ), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x7a29dd0699e0>(*(), **{'input_tensors': FakeTensor(..., device='cuda:0', size=(4, 8, 32)), 'dim': 1}):
cat() received an invalid combination of arguments - got (dim=int, input_tensors=FakeTensor, ), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''