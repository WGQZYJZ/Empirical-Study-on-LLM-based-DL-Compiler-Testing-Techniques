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
        self.linear = Linear(2, 4)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other
        v3 = torch.nn.functional.relu(v1)
        return v3


func = Model().to('cpu')


x = torch.randn(1, 2)

test_inputs = [x]
