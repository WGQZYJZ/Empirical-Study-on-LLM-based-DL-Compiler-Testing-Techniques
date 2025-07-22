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

    def __init__():
        super().__init__()
        self.linear = torch.nn.Linear(36, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 36)

test_inputs = [x1]
