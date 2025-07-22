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

    def __init__(self, min_value=0, max_value=1):
        super().__init__()

    def forward(self, x1):
        v0 = (x1 * 0.8959889827464012)
        v1 = (x1 + x1)
        v2 = torch.mean(v1, dim=[(- 2), (- 1)], keepdim=True)
        v3 = (v1 / v2)
        v4 = (v3 * 0.3452390219632011)
        v5 = torch.min(v4, torch.tensor(0.760402547351158, requires_grad=True), dim=[(- 2), (- 1)], keepdim=True)
        v6 = torch.max(v5, torch.tensor((- 0.42610920540287), requires_grad=True), dim=[(- 2), (- 1)], keepdim=True)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 3, 48, 48)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
min() received an invalid combination of arguments - got (Tensor, Tensor, keepdim=bool, dim=list), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
      didn't match because some of the keywords were incorrect: keepdim, dim
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


jit:
Failed running call_function <built-in method min of type object at 0x7f98bd0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 48, 48)), FakeTensor(..., size=(), requires_grad=True)), **{'dim': [-2, -1], 'keepdim': True}):
min() received an invalid combination of arguments - got (FakeTensor, FakeTensor, keepdim=bool, dim=immutable_list), but expected one of:
 * (Tensor input, *, Tensor out)
 * (Tensor input, Tensor other, *, Tensor out)
      didn't match because some of the keywords were incorrect: keepdim, dim
 * (Tensor input, int dim, bool keepdim, *, tuple of Tensors out)
 * (Tensor input, name dim, bool keepdim, *, tuple of Tensors out)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''