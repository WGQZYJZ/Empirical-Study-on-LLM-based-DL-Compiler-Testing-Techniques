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
        self.linear1 = torch.nn.Linear(64)

    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = v1 + x2
        return v2


func = Model().to('cpu')


o = torch.randn(1, 64)
x1 = 1

test_inputs = [o, x1]
