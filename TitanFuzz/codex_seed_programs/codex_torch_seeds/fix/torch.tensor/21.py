'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
print('\n\nTask 1: import PyTorch')
import torch
print('\n\nTask 2: Generate input data')
data = [[1, 2], [3, 4]]
print('\n\nTask 3: Call the API torch.tensor')
tensor_data = torch.tensor(data)
print(tensor_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor\ntorch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False)\n'
print('\n\nTask 1: import PyTorch')
import torch
print('\n\nTask 2: Generate input data')
data = [[1, 2], [3, 4]]
print('\n\nTask 3: Call the API torch.tensor')
tensor_data = torch.tensor(data, dtype=torch.float32)
print(tensor_data)