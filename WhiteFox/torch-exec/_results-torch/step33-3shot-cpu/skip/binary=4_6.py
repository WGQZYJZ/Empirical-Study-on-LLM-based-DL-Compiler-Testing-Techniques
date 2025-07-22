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
        self.linear1 = torch.addmm(torch.nn.Linear(20, 20), torch.nn.Linear(20, 20), torch.nn.Linear(20, 20))

    def forward(self, x0, x1, x2):
        v0 = self.linear1(x0)
        v1 = torch.linear(x1)
        v2 = torch.linear(x2)
        return (v0 + v1, v0 + v2)


func = Model().to('cpu')


x0 = torch.randn(10, 20)

x1 = torch.randn(10, 20)

x2 = torch.randn(10, 20)

test_inputs = [x0, x1, x2]
