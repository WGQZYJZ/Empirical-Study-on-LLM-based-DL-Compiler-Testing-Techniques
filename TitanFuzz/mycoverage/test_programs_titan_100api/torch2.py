import torch
input = torch.randn(3, 5)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
