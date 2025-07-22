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
        self.proj = torch.nn.Linear(inp_dim, inp_dim)
        self.scale = np.power(inp_dim, -0.5)

    def forward(self, x1, x2):
        q = 2 * x1 - 1
        k = self.proj(2 * x2 - 1)
        v = 2 * x2 - 1
        scaled_qkv = torch.matmul(q, k.transpose(-2, -1)).mul_(self.scale).softmax(dim=-1)
        output = scaled_qkv.matmul(v)
        return output


func = Model().to('cpu')

x1 = 1
x2 = 1

test_inputs = [x1, x2]
