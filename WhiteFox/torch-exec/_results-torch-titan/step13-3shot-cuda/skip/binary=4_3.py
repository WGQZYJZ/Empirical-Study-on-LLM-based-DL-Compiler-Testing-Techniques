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
        self.linear = Linear(n, m)
        self.linear1 = Linear(m, m)
        self.linear2 = Linear(m, m)

    def forward(self, input, other):
        x = self.linear(input)
        x = (x + other)
        x = self.linear1(x)
        x = (x + other)
        x = self.linear2(x)
        return x




func = Model().to('cuda')



input = torch.randn(1, 23)



other = torch.randn(30, 23)


test_inputs = [input, other]
