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

class TorchLinearModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.weight = torch.nn.Parameter(torch.rand(in_features=3, out_features=1, requires_grad=True))

    def forward(self, x):
        y = torch.nn.functional.linear(x, self.weight)
        z = y + x
        return z


func = TorchLinearModel().to('cpu')


x = torch.randn(1, 3)

test_inputs = [x]
