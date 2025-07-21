import torch
input = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
result = torch.equal(input, other)