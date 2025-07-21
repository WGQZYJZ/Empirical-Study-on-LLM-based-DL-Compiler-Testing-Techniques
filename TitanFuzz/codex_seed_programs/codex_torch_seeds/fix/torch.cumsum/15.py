'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.rand(3, 4, 5)
print(input_data)
print(torch.cumsum(input_data, dim=1))
print(torch.cumsum(input_data, dim=2))
print(torch.cumsum(input_data, dim=0))
print(torch.cumsum(input_data, dim=1, dtype=torch.int32))
output = torch.zeros(3, 4, 5, dtype=torch.int32)