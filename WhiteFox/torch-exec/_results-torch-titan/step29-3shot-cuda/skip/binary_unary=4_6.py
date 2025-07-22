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

    def __init__(self, other):
        super().__init__()
        self.linear_transform = Linear(8, 3)

    def forward(self, x1):
        v1 = self.linear_transform(x1)
        v2 = (v1 + other)
        v3 = relu(v2)
        return v3



other = 1

func = Model(other).to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]
