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

    def __init__(self, d_model, d_k, d_v):
        super().__init__()
        self.fc_k = torch.nn.Linear(d_model, d_k)
        self.fc_v = torch.nn.Linear(d_model, d_v)
        self.scaled_dot_product = ScaledDotProductAttention(temperature=d_k ** 0.5)

    def forward(self, x1, x2, x3):
        k = self.fc_k(x1)
        v = self.fc_v(x2)
        return self.scaled_dot_product(k, v, x3)


d_model = 1
d_k = 1
d_v = 1
func = Model(100, 25, 40).to('cpu')


x1 = torch.randn(3, 100)

x2 = torch.randn(2, 100)

x3 = torch.randn(1, 25)

test_inputs = [x1, x2, x3]
