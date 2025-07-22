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



class UserDataset(Dataset):

    def __getitem__(self, idx):
        if (idx == 0):
            return (x1, x2, torch.tensor(0))
        if (idx == 1):
            return (x1, x2, torch.tensor(1))
        if (idx == 2):
            return (x1, x2, torch.tensor(2))
        if (idx == 3):
            return (x1, x2, torch.tensor(3))
        if (idx == 4):
            return (x1, x2, torch.tensor(3))

    def __len__(self):
        return 5




class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 11, 1, stride=1, padding=1)

    def forward(self, x1):
        return self.conv(x1)




class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        return self.gelu(x1)




class Model3(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.pool = torch.nn.MaxPool2d(32)

    def forward(self, x1):
        v1 = self.pool(x1)
        v2 = (v1 - 1.0)
        return v2




class Model4(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 9)

    def forward(self, x):
        return self.linear(x)



func = UserDataset().to('cuda')



x1 = torch.randn(5, 3, 32, 32)



x2 = torch.randn(5, 3, 32, 32)


test_inputs = [x1, x2]
