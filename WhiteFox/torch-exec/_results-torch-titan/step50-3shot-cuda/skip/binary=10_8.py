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
        self.conv = torch.nn.Linear(10, 50)

    def forward(self, x1, x2=tensor):
        v1 = self.conv(x1)
        v2 = (v1 + x2)
        return v2



func = Model().to('cuda')



tensor = torch.randn(50)



x1 = torch.randn(10)



x2 = torch.randn(50)


test_inputs = [tensor, x1, x2]
