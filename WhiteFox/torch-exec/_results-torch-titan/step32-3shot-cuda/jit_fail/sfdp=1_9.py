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
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, in_features_1):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(inv_scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = self.dropout(v3)
        output = v4.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 3, 64, 1)



key = torch.randn(1, 3, 1, 64)



inv_scale_factor = torch.randn(1)


test_inputs = [query, key, inv_scale_factor]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''