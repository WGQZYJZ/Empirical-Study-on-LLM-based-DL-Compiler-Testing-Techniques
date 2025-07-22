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
        self.permute = torch.nn.Permute([0, 2, 1])
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.permute(x1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2.permute(0, 2, 1)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]
