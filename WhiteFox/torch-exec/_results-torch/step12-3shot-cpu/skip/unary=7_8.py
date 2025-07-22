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
        self.l1 = torch.nn.Linear(3, 12, has_bias=False)

    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = v1 * torch.clamp(input=v1 + 3, min=0, max=6)
        v3 = v2 / 6
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 4)

test_inputs = [x1]
