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
        self.perm1 = torch.nn.Permute([0, 2, 1])
        self.perm2 = torch.nn.Permute([0, 2, 1])
        self.perm3 = torch.nn.Permute([0, 2, 1])
        self.perm4 = torch.nn.Permute([0, 2, 1])
        self.perm5 = torch.nn.Permute([0, 2, 1])

    def forward(self, x1, x2):
        o1 = x1.permute(0, 2, 1)
        o2 = x2
        o3 = self.perm1(x1)
        o4 = self.perm2(o1)
        o5 = self.perm3(o2)
        o6 = self.perm4(o3)
        o7 = torch.bmm(o5, o6)
        o8 = self.perm5(o7)
        return torch.bmm(o8, o7)



func = Model1().to('cpu')


x1 = torch.randn(1, 2, 2)

x2 = torch.randn(1, 2, 2)

test_inputs = [x1, x2]
