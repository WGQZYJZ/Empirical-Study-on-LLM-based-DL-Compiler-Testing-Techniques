import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, x1, x2, x3, x4, x5, x6):
        h1 = torch.mm(x1, x2)
        h2 = torch.mm(x1, x2)
        h3 = torch.mm(x3, x4)
        h4 = torch.mm(x5, x6)
        return h1 + h2 + h3 + torch.mm( x1, x3 ) + h4
m = Model()
# Inputs to the model
x1 = torch.randn( 4, 4)
x2 = torch.randn( 4, 4)
x3 = torch.randn( 4, 4)
x4 = torch.randn( 4, 4)
x5 = torch.randn( 4, 4)
x6 = torch.randn( 4, 4)
