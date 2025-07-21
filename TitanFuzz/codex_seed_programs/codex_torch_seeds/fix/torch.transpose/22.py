'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input = torch.randn(3, 4)
output = torch.transpose(input, 0, 1)
print(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, dtype=None, device=None, requires_grad=False)\n'
import torch
data = [[1, 2], [3, 4]]
output = torch.tensor(data, dtype=torch.float32, device=torch.device('cuda'), requires_grad=True)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, dtype=None, device=None, requires_grad=False)\n'