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
        self.q = torch.nn.Linear(m, n, bias=False)
        self.k = torch.nn.Linear(m, n, bias=False)
        self.v = torch.nn.Linear(n, n)

    def forward(self, q, k, v):
        q = self.q(q)
        k = self.k(k).transpose(-2, -1)
        v = self.v(v)
        w = torch.matmul(q, k)
        w = w / math.sqrt(n)
        w = w + attn_mask
        w = torch.softmax(w, dim=-1)
        output = torch.matmul(w, v)
        return output


func = Model().to('cpu')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]
