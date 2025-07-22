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
        self.fc = torch.nn.Linear(3, 3)

    def forward(self, x1):
        x1 = self.fc(x1)
        split_tensors = torch.split(x1, [-1, 1], 1)
        concatenated_tensor = torch.cat(split_tensors, 1)
        return (concatenated_tensor, torch.split(x1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 3)

test_inputs = [x1]
