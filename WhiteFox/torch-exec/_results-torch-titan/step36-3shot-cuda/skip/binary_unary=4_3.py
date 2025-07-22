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
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x2, x3=0.5):
        v1 = self.linear(x2)
        v3 = (v1 + x3)
        v2 = torch.relu(v3)
        return v2



other = 1
func = Model(other, x3=2).to('cuda')



x2 = torch.randn(1, 3, 5, 5)


test_inputs = [x2]
