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
        self.attention = Attention()

    def forward(self, x1, x2, x3):
        (b1, l1, e1) = x1.size()
        (b2, l2, e2) = x2.size()
        (b3, l3, e3) = x3.size()
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 * e2 ** (-0.5)
        v3 = F.softmax(v2, dim=-1)
        v4 = F.dropout(v3, p=0.5)
        v5 = torch.matmul(v4, x3)
        return v5


func = Model().to('cpu')


x1 = torch.randn(48, 10, 64)

x2 = torch.randn(48, 10, 64)

x3 = torch.randn(48, 10, 64)

test_inputs = [x1, x2, x3]
