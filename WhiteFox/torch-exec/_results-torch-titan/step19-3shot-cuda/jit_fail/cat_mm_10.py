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
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        return torch.cat(x1, x2, v1, v2)




func = Model().to('cuda')



x1 = torch.randn(1, 6)



x2 = torch.randn(6, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor, Tensor, Tensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
      didn't match because some of the arguments have invalid types: (!Tensor!, !Tensor!, !Tensor!, Tensor)
 * (tuple of Tensors tensors, name dim, *, Tensor out)
      didn't match because some of the arguments have invalid types: (!Tensor!, !Tensor!, !Tensor!, Tensor)


jit:
Failed running call_function <built-in method cat of type object at 0x77daade699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 6)), FakeTensor(..., device='cuda:0', size=(6, 1)), FakeTensor(..., device='cuda:0', size=(1, 1)), FakeTensor(..., device='cuda:0', size=(1, 1))), **{}):
cat() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor, FakeTensor), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !FakeTensor!)
 * (tuple of Tensors tensors, name dim, *, Tensor out)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !FakeTensor!)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''