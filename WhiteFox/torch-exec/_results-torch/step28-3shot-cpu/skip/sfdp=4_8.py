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
        self.attn = torch.nn.MultiheadAttention(H, num_heads)

    def forward(self, x1, x2, x3):
        v1 = self.attn(x1, x2, x2)
        v2 = self.attn(v1[1], x3, x3)
        return v2[0]


func = Model().to('cpu')


H = 8
T = 3
B = 3
x1 = torch.randn(B, T, H)

H = 8
T = 3
B = 3
x2 = torch.randn(B, T, H)

H = 8
T = 3
B = 3
x3 = torch.randn(B, T, H)

test_inputs = [x1, x2, x3]
