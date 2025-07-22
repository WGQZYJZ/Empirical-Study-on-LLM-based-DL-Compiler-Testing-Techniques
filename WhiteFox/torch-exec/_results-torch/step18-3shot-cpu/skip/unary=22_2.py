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
        self.layer1 = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        v1 = self.layer1(x)
        v2 = torch.tanh(v1)
        return v2


func = Model().to('cpu')

x = 1

test_inputs = [x]
