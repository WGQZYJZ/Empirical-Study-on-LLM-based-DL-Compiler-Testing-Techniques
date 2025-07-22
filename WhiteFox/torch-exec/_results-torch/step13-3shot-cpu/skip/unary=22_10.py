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
        self.linear = torch.nn.Linear(64, 32)
        self.linear.apply(init_weights)

    def forward(self, x1):
        v0 = x1.detach().clone()
        v0.requires_grad_(True)
        v1 = self.linear(v0)
        v2 = torch.tanh(v1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 64)

test_inputs = [x1]
