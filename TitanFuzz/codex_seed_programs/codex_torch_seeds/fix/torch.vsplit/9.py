'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vsplit\ntorch.vsplit(input, indices_or_sections)\n'
import torch
data = torch.arange(0, 16).reshape(4, 4)
print(data)
result = torch.vsplit(data, 4)
print(result)
result = torch.vsplit(data, 2)
print(result)
'\nTask 4: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
result = torch.hsplit(data, 4)
print(result)
result = torch.hsplit(data, 2)
print(result)
'\nTask 5: Call the API torch.split\ntorch.split(input, indices_or_sections, dim)\n'
result = torch.split(data, 4, dim=0)
print(result)
result = torch.split(data, 2, dim=0)
print