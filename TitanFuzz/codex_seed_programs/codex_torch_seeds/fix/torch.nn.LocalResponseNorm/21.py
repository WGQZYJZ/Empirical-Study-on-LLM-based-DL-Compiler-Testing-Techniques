'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 5, 10, 10)
norm = nn.LocalResponseNorm(5, alpha=0.0001, beta=0.75, k=1.0)
output = norm(input)
print(output)