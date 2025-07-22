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

    def __init__(self, requires_grad):
        super().__init__()
        self.x = torch.randn(3, requires_grad=requires_grad)

    def forward(self, y):
        return y + self.x


requires_grad = 1

func = Model(requires_grad).to('cpu')


y = torch.randn(3, requires_grad=True)

test_inputs = [y]
