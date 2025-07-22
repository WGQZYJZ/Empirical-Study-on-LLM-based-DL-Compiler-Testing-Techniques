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

    def __init__(self, dim=256):
        super().__init__()
        self.linear = torch.nn.Linear(20, dim)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        return v1 + x2


func = Model(dim).to('cpu')


x1 = torch.randn(4, 20)

dim = 256
x2 = torch.randn(4, dim)

test_inputs = [x1, x2]
