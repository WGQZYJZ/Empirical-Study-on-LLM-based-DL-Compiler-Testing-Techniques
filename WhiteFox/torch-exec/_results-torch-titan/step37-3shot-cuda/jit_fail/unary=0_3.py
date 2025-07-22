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
        self.conv = torch.nn.Conv2d(3, 3, 10, stride=1, padding=4)

    def forward(self, x5):
        v1 = self.conv(x5)
        v2 = torch.tensor(0.09409731, 'requires_grad=True')
        v3 = torch.tensor(0.06180918, 'requires_grad=True')
        v4 = (v3 * v3)
        v5 = (v4 + torch.tensor(0.0382815, 'requires_grad=True'))
        v6 = (v1 * v5)
        v7 = (v6 * 0.05913217)
        v8 = (v1 * v1)
        v9 = torch.tensor(0.01184593, 'requires_grad=True')
        v10 = torch.tensor(0.05406853, 'requires_grad=True')
        v11 = (v10 + torch.tensor(0.00940389, 'requires_grad=True'))
        v12 = (v8 * v11)
        v13 = (v12 * 0.08843533)
        v14 = torch.pow(v1, 'scalar')
        v15 = (v14 * torch.tensor((- 0.09118476), 'requires_grad=True'))
        v16 = (v15 + v13)
        v17 = (v16 + v7)
        v18 = torch.tensor((- 0.03596627), requires_grad=True)
        v19 = torch.tensor(True, 'requires_grad=True')
        v20 = torch.tensor(0.04154189, 'requires_grad=True')
        v21 = torch.tensor(0.05737904, 'requires_grad=True')
        v22 = (v21 + v19)
        v23 = (v22 * torch.tensor(0.04536779, 'requires_grad=True'))
        v24 = torch.pow(v17, 'scalar')
        v25 = (v24 * v23)
        v26 = (v25 + v20)
        v27 = (v26 + v18)
        v28 = torch.tensor(0.05688172, 'requires_grad=True')
        v29 = (v27 * v28)
        return v29




func = Model().to('cuda')



x5 = torch.randn(1, 3, 32, 32)


test_inputs = [x5]

# JIT_FAIL
'''
direct:
tensor() takes 1 positional argument but 2 were given

jit:
Failed running call_function <built-in method tensor of type object at 0x74236bc699e0>(*(0.09409731, 'requires_grad=True'), **{}):
tensor() takes 1 positional argument but 2 were given

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''