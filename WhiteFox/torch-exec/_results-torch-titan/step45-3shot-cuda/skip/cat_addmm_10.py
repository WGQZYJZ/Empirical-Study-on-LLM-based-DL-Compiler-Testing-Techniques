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
        self.layers = nn.Linear(3, 4, bias=False)
        self.matmul = torch.matmul
        self.expand = self.layers.expand(3, 3)

    def forward(self, x):
        x = self.layers(x)
        x = self.matmul(self.expand, x)
        return torch.squeeze(x, 1)




func = Model().to('cuda')



x = torch.randn(2, 1)


test_inputs = [x]
