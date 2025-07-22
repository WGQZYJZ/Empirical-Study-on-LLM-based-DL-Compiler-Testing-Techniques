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
        self.fc1 = torch.nn.Linear(...)

    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = torch.matmul(x2, v1.transpose(0, 1))
        return v2


func = Model().to('cpu')


x1 = torch.randn(2, 5)

x2 = torch.randn(3, 5)

test_inputs = [x1, x2]
