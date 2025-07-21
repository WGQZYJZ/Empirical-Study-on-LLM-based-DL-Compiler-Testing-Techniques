import torch

input = torch.randn(4, 4)
output = torch.abs(input)
torch.abs_(input)