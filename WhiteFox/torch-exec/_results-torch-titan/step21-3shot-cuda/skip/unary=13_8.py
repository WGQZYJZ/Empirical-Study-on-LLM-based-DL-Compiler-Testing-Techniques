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
        s1 = torch.nn.Linear(1, 5)
        s2 = torch.sigmoid
        n1 = torch.nn.Linear(1, 3)
        n2 = torch.nn.Sigmoid
        p1 = torch.nn.Linear(3, 1)
        self.s = torch.nn.Sequential(s1, s2, p1)
        self.n = torch.nn.Sequential(n1, n2, p1)

    def forward(self, x1):
        v1s = self.s(x1)
        v2s = self.n(x1)
        v1n = self.n(x1)
        v2n = self.n(x1)
        out = ((((v1s * v2s) + (v1s * v2n)) + (v1n * v2s)) + (v1n * v2n))
        return out



func = Model().to('cuda')



x1 = torch.randn(1, 1)


test_inputs = [x1]
