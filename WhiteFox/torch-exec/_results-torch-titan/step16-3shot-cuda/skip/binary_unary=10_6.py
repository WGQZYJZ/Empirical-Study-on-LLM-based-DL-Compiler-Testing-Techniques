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
        self.linear = torch.nn.Linear(1, 5)
        self.linear_copy = copy.deepcopy(self.linear)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.add(v1, self.linear_copy)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



weights = torch.tensor([[1.9]])



x1 = torch.tensor([[3.2]])


test_inputs = [weights, x1]
