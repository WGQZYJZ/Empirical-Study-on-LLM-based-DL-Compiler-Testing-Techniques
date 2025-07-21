import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, inp1, inp2):
        return inp1(x, inp2)
m = Model()
# Inputs to the model
x = torch.randn(3, 3, requires_grad=True)
inp = [
    (torch.nn.functional.adaptive_avg_pool2d, dict(output_size=3), torch.randn(3, 3)),
    (torch.transpose, (), torch.randn(3, 3))
]
