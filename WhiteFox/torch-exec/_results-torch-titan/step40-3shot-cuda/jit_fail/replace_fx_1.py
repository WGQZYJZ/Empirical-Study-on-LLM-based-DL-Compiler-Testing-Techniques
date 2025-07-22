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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.dropout(torch.rand_like(x1), p=0.1)




class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x1 = torch.rand_like(x1)
        x2 = (x1 + 6)
        return F.dropout(x2, p=0.2, training=True)




class Model3(torch.nn.Module):

    def __init__(self, model1, model2):
        super().__init__()
        self.model1 = model1
        self.model2 = model2

    def forward(self, x1):
        x2 = self.model1(x1)
        x3 = self.model2(x2)
        return x3



model1 = 1
model2 = 1

func = Model3(model1, model2).to('cuda')



p1 = torch.randn(2, 2)



x1 = torch.randn(1, 2, 2)


test_inputs = [p1, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''