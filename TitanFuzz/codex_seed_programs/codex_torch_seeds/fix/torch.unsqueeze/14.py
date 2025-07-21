'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
import torch
input = torch.ones(1, 1, 2, 2, 2)
output = torch.unsqueeze(input, dim=0)
print(output)
output = torch.unsqueeze(input, dim=1)
print(output)
output = torch.unsqueeze(input, dim=4)
print(output)
output = torch.unsqueeze(input, dim=(- 1))
print(output)
output = torch.unsqueeze(input, dim=(- 3))
print(output)