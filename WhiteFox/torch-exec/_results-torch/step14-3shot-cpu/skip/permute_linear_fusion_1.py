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
        self.linear = torch.nn.Linear(2, 2)
        self.layer_norm = torch.nn.LayerNorm(shape=(2, 2))

    def forward(self, x1):
        v1 = self.layer_norm(x1)
        v2 = x1.permute(0, 2, 1)
        v3 = torch.tensor([[[0.0, 1.0]], [[1.0, 0.0]]], requires_grad=True)
        v3 = v3.to(device=v1.device, dtype=v1.dtype)
        self.linear.weight = v3
        return self.linear(v2)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]
