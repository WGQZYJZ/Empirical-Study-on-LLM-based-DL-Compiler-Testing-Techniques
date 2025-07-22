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
        self.layer = torch.nn.Linear(2, 2)

    def forward(self, x1):
        n = torch.numel(self.layer.weight)
        m3 = torch.zeros(n, device=self.layer.weight.device)
        m4 = torch.tensor(0, device=self.layer.weight.device)
        i = 0
        j = 0
        while (i < len(m3)):
            m3[i] += self.layer.weight[((i // 2), (i % 2))]
            m4 += self.layer.weight[((i // 2), (i % 2))]
            i += 1
        return ((torch.cat([x1, self.layer.weight.unsqueeze(0)], dim=0) + n) - m4)




func = Model().to('cuda')



x1 = torch.randn(2, 1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
result type Float can't be cast to the desired output type Long

jit:
Failed running call_function <built-in method cat of type object at 0x7fd0002699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 1, 2)), FakeTensor(..., device='cuda:0', size=(1, 2, 2), requires_grad=True)],), **{'dim': 0}):
Sizes of tensors must match except in dimension 0. Expected 1 but got 2 for tensor number 1 in the list

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''