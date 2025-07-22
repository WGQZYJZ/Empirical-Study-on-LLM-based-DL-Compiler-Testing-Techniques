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
        self.linear = torch.nn.Linear(12, 64)
        self.other = torch.autograd.Variable(torch.Tensor([...]))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - self.other)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 12)


test_inputs = [x1]
