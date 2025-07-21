'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
print(torch.cumsum(input_data, dim=0))
print(torch.cumsum(input_data, dim=0, dtype=torch.float))
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(torch.cumsum(input_data, dim=1))