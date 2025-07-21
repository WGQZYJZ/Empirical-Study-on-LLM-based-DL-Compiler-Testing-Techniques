'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3, 5, 5)
lrn = nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input_data)
print(output)