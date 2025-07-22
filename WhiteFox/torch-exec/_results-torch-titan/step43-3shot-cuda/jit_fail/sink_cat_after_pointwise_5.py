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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.rand = random.randint(0, 1)

    def forward(self, x):

        def concat_in_dim(x):
            return [torch.cat(x, dim=1), torch.cat(x, dim=1)]

        def concat_in_dim2(x):
            return [torch.cat(x, dim=2), torch.cat(x, dim=2)]

        def concat_in_dim3(x):
            return [torch.cat(x, dim=3), torch.cat(x, dim=3)]
        x = concat_in_dim([x, x, x])
        x = (concat_in_dim(x) if self.rand else x)
        x = (concat_in_dim(x) if self.rand else x)
        x = (concat_in_dim(x) if self.rand else x)
        x = (concat_in_dim2(x) if self.rand else x)
        x = (concat_in_dim3(x) if self.rand else x)
        x = torch.relu(x)
        x = x[0]
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4, 5, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
relu(): argument 'input' (position 1) must be Tensor, not list

jit:
Failed running call_function <built-in method relu of type object at 0x77d75a4699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 9, 4, 5, 6)), FakeTensor(..., device='cuda:0', size=(2, 9, 4, 5, 6))],), **{}):
relu(): argument 'input' (position 1) must be Tensor, not immutable_list

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''