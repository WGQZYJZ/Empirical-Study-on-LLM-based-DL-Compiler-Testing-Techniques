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



class Scores(torch.nn.Module):

    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, x1, x2):
        Q = x1
        K = (x1 if (x2 is None) else x2)
        qk = torch.matmul(Q, torch.transpose(K, (- 2), (- 1)))
        scale_factor = np.power(np.float32(K.size(self.dim)), (- 0.5))
        softmax_qk = torch.softmax((qk * scale_factor), dim=(- 1))
        dropout_qk = softmax_qk
        output = torch.matmul(dropout_qk, V)
        return output



dim = 1

func = Scores(dim).to('cuda')



x1 = torch.randn(1, 3, 64)

x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
transpose() received an invalid combination of arguments - got (int, int, int), but expected one of:
 * (Tensor input, int dim0, int dim1)
      didn't match because some of the arguments have invalid types: (!int!, int, int)
 * (Tensor input, name dim0, name dim1)
      didn't match because some of the arguments have invalid types: (!int!, !int!, !int!)


jit:
Failed running call_function <built-in method transpose of type object at 0x76e4624699e0>(*(1, -2, -1), **{}):
transpose() received an invalid combination of arguments - got (int, int, int), but expected one of:
 * (Tensor input, int dim0, int dim1)
      didn't match because some of the arguments have invalid types: (!int!, int, int)
 * (Tensor input, name dim0, name dim1)
      didn't match because some of the arguments have invalid types: (!int!, !int!, !int!)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''