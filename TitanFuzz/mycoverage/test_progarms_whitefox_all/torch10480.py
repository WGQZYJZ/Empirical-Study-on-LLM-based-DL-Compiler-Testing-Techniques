import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x1, x2):
        torch.cat([torch.mm(x1, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2)], 1)
        return torch.cat([torch.mm(x2, x2), torch.mm(x2, x2), torch.mm(x2, x2), x2, torch.mm(x2, x2)], 1)
m = Model()
# Inputs to the model
x1 = torch.randn(1, 1)
x2 = torch.randn(256, 512)
