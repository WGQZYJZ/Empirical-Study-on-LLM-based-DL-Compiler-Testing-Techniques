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

    def __init__(self, __in_features, __out_features):
        super().__init__()
        self.linear = torch.nn.Linear(__in_features, __out_features)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2



__in_features = 1
__out_features = 1
func = Model(16, 32).to('cuda')



x1 = torch.randn(224, 224)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (224x224 and 16x32)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(224, 224)),), **{}):
a and b must have same reduction dim, but got [224, 224] X [16, 32].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''