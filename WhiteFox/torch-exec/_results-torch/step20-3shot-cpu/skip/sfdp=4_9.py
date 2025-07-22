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

    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads

    def forward(self, x, x):
        q = x.reshape((-1, self.num_heads, x.shape[-1]))
        k = x.reshape((-1, self.num_heads, x.shape[-1]))
        v = x.reshape((-1, self.num_heads, x.shape[-1]))
        qk = q @ k.transpose(-2, -1)
        a = qk / math.cbrt(q.size(-1))
        return a


num_heads = 1
func = Model(4).to('cpu')


x1 = torch.randn(1, 16, 8)
x = 1

test_inputs = [x1, x]
