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
        self.linear = torch.nn.Linear(2, 1, bias=False)

    def forward(self, x1):
        o1 = self.linear(x1)
        o2 = (o1 * torch.clamp((o1 + 3), min=0, max=6))
        return (o2 / 6)



func = Model().to('cuda')



x1 = torch.randn(1, 2).requires_grad_()


x1 = torch.randn(1, 2).requires_grad_()



x1 = torch.randn(1, 2).requires_grad_()


dy = torch.ones_like(x1, device=x1.device)


x1 = torch.randn(1, 2).requires_grad_()


dy = torch.ones_like(x1, device=x1.device)


y_num = (x1.data * dy).sum()


dy = torch.ones_like(x1, device=x1.device)


y_den = dy.sum()


test_inputs = [x1, dy, y_num, y_den]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''