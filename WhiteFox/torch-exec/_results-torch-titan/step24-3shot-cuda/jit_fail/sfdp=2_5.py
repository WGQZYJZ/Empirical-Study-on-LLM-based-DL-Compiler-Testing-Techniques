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

    def __init__(self, hidden, in_features, out_features, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, x, weight):
        v1 = torch.matmul(x, weight.transpose((- 2), (- 1)))
        v2 = v1.div((self.in_features ** 0.5))
        v3 = torch.softmax(v2, dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, self.dropout_p, training=self.training)
        v5 = torch.matmul(v4, weight)
        return v5



hidden = 1
in_features = 1
out_features = 1
dropout_p = 1
func = Model(32, 64, 100, 0.1).to('cuda')



x = torch.randn(28, 64)



weight = torch.randn(100, 64)


test_inputs = [x, weight]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'in_features'

jit:
in_features

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''