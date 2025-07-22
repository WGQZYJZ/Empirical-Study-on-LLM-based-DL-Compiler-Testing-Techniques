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

    def forward(self, __input_tensors__):
        cat_input_tensors = torch.cat(__input_tensors__, dim=1)
        sliced_tensor = cat_input_tensors[:, 0:9223372036854775807]
        cat_sliced_tensor = sliced_tensor[:, 0:size]
        all_tensors = [cat_input_tensors, cat_sliced_tensor]
        all_tensors = torch.cat(all_tensors, dim=1)
        return all_tensors




func = Model().to('cuda')

__input_tensors__ = 1

test_inputs = [__input_tensors__]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x7d41f5a699e0>(*(1,), **{'dim': 1}):
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''