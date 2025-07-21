'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_data)
print(torch.all(input_data))
print(torch.all(input_data, dim=0))
print(torch.all(input_data, dim=1))
print(torch.all(input_data, dim=1, keepdim=True))
print(torch.all(input_data, dim=(- 1)))