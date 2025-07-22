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
        self.linear = torch.nn.Linear(in_features, out_features, bias=bias)

    def forward(self, input, other):
        return (self.linear(input) + other)



func = Model().to('cuda')

input = 1
other = 1

test_inputs = [input, other]
