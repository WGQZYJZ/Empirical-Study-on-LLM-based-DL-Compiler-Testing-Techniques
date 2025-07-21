'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input = torch.randn(1, 2, 3, 4)
output = torch.unsqueeze(input, dim=0)
print(output)