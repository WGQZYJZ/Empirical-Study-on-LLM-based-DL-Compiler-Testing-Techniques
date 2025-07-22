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

    def forward(self, x1, x2):
        return torch.cat(1.1)




func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(1, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat(): argument 'tensors' (position 1) must be tuple of Tensors, not float

jit:
Failed running call_function <built-in method cat of type object at 0x751e56a699e0>(*(1.1,), **{}):
cat(): argument 'tensors' (position 1) must be tuple of Tensors, not float

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''