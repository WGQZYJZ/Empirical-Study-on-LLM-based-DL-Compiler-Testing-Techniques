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



class model(nn.Module):

    def __init__(self):
        super(model, self).__init__()
        self.conv_t = nn.ConvTranspose2d(1, 1, 3)

    def forward(self, x):
        x = self.conv_t(x)
        return x[:, :, 1:4:2, 2:4]




func = model().to('cuda')



x1 = []


x1 = torch.tensor(x1, requires_grad=True)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [0]

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(0,)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [0]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''