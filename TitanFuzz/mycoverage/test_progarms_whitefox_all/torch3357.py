import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2

m = Model()
# Initializing the model
m = Model(in_features=2048, out_features=1)

# Inputs to the model
x1 = torch.randn(1, 2048)
