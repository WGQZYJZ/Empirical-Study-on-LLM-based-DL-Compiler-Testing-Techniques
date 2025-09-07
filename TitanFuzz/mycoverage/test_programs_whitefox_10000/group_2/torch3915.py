import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTra

m = Model()
x1 = torch.randn(1, 32, 20, 20)
