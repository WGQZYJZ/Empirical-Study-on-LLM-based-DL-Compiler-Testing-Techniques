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

    def __init__(self, p):
        super().__init__()
        self.p = p

    def forward(self, q, k, v, inf=1000000000.0):
        t1 = torch.matmul(q, k.transpose(-2, -1))
        s1 = t1.div(self.p.i1)
        t2 = torch.nn.functional.softmax(s1, dim=-1)
        t3 = torch.nn.functional.dropout(t2, p=self.p.d0)
        t4 = torch.matmul(t3, v)
        return t4


p = Param()
func = Model(p).to('cpu')


q = torch.randn(1, 40, 20)

k = torch.randn(1, 60, 20)

v = torch.randn(1, 60, 5)

test_inputs = [q, k, v]
