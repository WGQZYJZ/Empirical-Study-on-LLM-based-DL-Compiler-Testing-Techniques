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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(nn.ReLU(), nn.Linear(2, 4))

    def forward(self, x):
        x = self.layers(x)
        x = torch.reshape(x, [2, 1, 4, 1])
    return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]
