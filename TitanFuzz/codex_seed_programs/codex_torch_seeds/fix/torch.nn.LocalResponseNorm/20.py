'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LocalResponseNorm\ntorch.nn.LocalResponseNorm(size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]], dtype=torch.float)
norm = nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = norm(input_data)
print(output)