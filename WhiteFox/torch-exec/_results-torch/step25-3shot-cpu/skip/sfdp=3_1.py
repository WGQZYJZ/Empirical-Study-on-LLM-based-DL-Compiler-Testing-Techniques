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

    def __init__(self, scale_factor=None, dropout_p=None):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p
        self.linear = torch.nn.Linear(6, 1)

    def forward(self, q, k, v):
        mul = q.matmul(k.transpose(1, 2))
        mul = mul / self.scale_factor
        softmax = nn.functional.softmax(mul, dim=-1)
        drop = nn.functional.dropout(softmax, p=self.dropout_p)
        out = drop.matmul(v)
        return out


func = Model(scale_factor, dropout_p).to('cpu')


q = torch.randn(5, 3, 6)

k = torch.randn(5, 12, 6)

v = torch.randn(5, 12, 6)

test_inputs = [q, k, v]
