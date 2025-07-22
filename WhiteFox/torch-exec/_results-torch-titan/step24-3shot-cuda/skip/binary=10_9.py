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
        self.linear = torch.nn.Linear(3, 4, 1, 2, 1, True)

    def forward(self, x, other):
        v1 = self.linear(x)
        v2 = (v1 + other)
        return (v2, (v2 * other))



func = Model().to('cuda')



x = torch.randn(1, 3)



other = torch.randn(1, 4)


test_inputs = [x, other]
