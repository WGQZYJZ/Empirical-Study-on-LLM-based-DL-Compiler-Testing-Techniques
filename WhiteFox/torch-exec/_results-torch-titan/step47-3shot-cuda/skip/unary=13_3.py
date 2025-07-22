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
        self.linear = torch.nn.Linear(6, 2, with_bias=True)

    def forward(self, x1):
        return x1



func = Model().to('cuda')



x1 = torch.randn(2, 6)


test_inputs = [x1]
