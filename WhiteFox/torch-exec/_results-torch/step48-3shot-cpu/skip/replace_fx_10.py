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
        self.x5 = torch.nn.Parameter(torch.tensor([[3, 0], [0, 4]]))

    def forward(self, x2, x3):
        t = torch.rand_like(x2)
        x1 = torch.nn.functional.gelu(t)
        t = F.dropout(x2, p=0.5) + x1
        t = t * x5
        t = torch.sin(t)
        return t



func = Model().to('cpu')


x2 = torch.randn([2, 2])

x3 = torch.randn([2, 2])

test_inputs = [x2, x3]
