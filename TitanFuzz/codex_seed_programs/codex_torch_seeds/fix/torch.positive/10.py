'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input = torch.randn(1, 3, 3, 3)
output = torch.positive(input)
print(output)