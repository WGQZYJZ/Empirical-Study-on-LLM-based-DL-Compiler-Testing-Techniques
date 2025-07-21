'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
input = torch.randn(2, 4, 4, 4)
lrn = torch.nn.LocalResponseNorm(2)
output = lrn(input)
print(output)