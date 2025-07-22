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
        self.linear = torch.nn.Linear(64, 16)

    def forward(self, x2):
        v0 = self.linear(x2)
        v1 = (v0 + torch.tensor([0.11162993170767403, 0.4021012740842126, (- 0.07421838647074475), 0.26406847390523197, 0.23260966332802727, 0.016116183662522165, 0.026168399269938296, (- 0.4989572945771398), 0.16524195617713364, (- 0.35611296942644854), 0.3153151985851663, 0.2846994441283839, 0.39923304879812777, (- 0.1077293147722334), 0.0744285980803726, (- 0.06619982140183794), 0.1789969787822284, (- 0.045829322652776866), 0.41095036289151365, (- 0.11422645138533231)]))
        v2 = torch.relu(v1)
        return v2



func = Model().to('cuda')



x2 = torch.randn(10, 64)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(10, 16)), FakeTensor(..., size=(20,))), **{}):
Attempting to broadcast a dimension of length 20 at -1! Mismatching argument at index 1 had torch.Size([20]); but expected shape should be broadcastable to [10, 16]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''