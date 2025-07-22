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

    def __init__(self, output_dim):
        super(Model, self).__init__()
        self.dense1 = torch.nn.Linear(2, output_dim)
        for (n, p) in self.dense1.named_parameters():
            if ('weight' in n):
                torch.nn.init.normal_(p, std=1.0)

    def forward(self, X, W):
        x1 = F.normalize(X, p=2, dim=1)
        d1 = self.dense(x1)
        return d1



output_dim = 1

func = Model(output_dim).to('cuda')



X = torch.randn(1, 2, requires_grad=True)



W = torch.empty(1, requires_grad=False)


test_inputs = [X, W]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dense'

jit:
dense

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''