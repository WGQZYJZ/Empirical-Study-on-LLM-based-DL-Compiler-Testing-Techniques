import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.embedding = torch.nn.Embedding(4, 2, padding_idx=1)
    def forward(self, x1, y1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = self.embedding(y1)[:, 2:, :]
        return v2, v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
y1 = torch.tensor([0])
