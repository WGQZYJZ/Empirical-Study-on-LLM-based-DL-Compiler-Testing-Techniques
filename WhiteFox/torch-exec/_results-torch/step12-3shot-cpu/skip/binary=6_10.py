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
        self.linear = torch.nn.Linear(int(input_size), int(hidden_size), bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - x1
        return v2


func = Model().to('cpu')

input_size = 37


x1 = torch.randn(1, int(input_size))

test_inputs = [x1]
