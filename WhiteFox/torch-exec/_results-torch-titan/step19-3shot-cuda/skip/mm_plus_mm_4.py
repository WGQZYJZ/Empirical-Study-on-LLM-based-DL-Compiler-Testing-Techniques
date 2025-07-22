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

    def __init__(self, shape1, shape2, shape3, shape4):
        super().__init__()
        self.layer1 = torch.nn.Linear(shape1, shape2)
        self.layer2 = torch.nn.Linear(shape2, shape3)
        self.layer3 = torch.nn.Linear(shape3, shape4)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        x = torch.mm(x, x)
        x = (x @ self.layer1)(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        return x




shape1 = (1, 1)


shape2 = (1, 1)


shape3 = (1, 1)


shape4 = (1, 1)


func = Model(shape1, shape2, shape3, shape4).to('cuda')

x = 1

test_inputs = [x]
