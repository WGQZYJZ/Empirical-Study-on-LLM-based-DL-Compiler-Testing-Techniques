'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input = torch.randn(1, 1, 3)
print(input)
output = torch.unsqueeze(input, dim=0)
print(output)
output = torch.unsqueeze(input, dim=1)
print(output)
output = torch.unsqueeze(input, dim=2)
print(output)