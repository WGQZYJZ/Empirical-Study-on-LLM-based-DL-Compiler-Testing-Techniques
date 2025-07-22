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
        self.attention = torch.nn.MultiheadAttention(n_head=16, d_model=64, dropout=0.1)

    def forward(self, x1, x2):
        return (self.attention(x1, x1, x2)[0], self.key(x2), self.value(x2))


func = Model().to('cpu')


x1 = torch.randn(1, 2, 3, 64, 64)

x2 = torch.randn(1, 3, 4, 64, 64)

test_inputs = [x1, x2]
