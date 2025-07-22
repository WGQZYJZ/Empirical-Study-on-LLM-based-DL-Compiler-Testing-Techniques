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

    def __init__(self, m, n, p, q):
        super().__init__()
        self.m = m
        self.n = n
        self.p = p
        self.q = q
        self.dropout = torch.nn.Dropout(p)
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.matmul5 = torch.matmul(self.m, self.n.transpose((- 2), (- 1)))

    def forward(self, x1):
        _scale_factor1 = torch.tensor((1 / 64.0))
        _scale_factor = _scale_factor1.to(torch.float32)
        v1 = torch.matmul(x1, self.matmul5)
        v2 = v1.mul(_scale_factor)
        v3 = self.softmax(v2)
        v4 = self.dropout(v3)
        v5 = torch.matmul(v4, self.q)
        return v5




m = Model()


n = torch.randn(512, 512)


p = 0.25


q = torch.randn(24, 512)


func = Model(m, n, p, q).to('cuda')



n = torch.randn(512, 512)



q = torch.randn(24, 512)



x1 = torch.randn(24, 512, 64)


test_inputs = [n, q, x1]
