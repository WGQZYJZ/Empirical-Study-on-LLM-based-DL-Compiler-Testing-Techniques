'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dist\ntorch.dist(input, other, p=2)\n'
import torch
input_data = torch.randn(1, 3)
other_data = torch.randn(1, 3)
print(input_data)
print(other_data)
torch.dist(input_data, other_data, p=2)