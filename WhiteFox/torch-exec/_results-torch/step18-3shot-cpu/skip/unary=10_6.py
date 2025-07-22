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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 10)

    def forward(self, x):
        x = x + 3
        x = torch.clamp(x, min=0)
        x = torch.clamp(x, max=6)
        x = self.linear(x)
        return x


func = Model().to('cpu')



x = torch.randn(1, 1, device=DEVICE)

test_inputs = [x]
