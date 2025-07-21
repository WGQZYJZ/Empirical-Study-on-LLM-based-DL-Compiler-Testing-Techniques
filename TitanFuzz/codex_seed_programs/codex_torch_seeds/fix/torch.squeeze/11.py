'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print(torch.__version__)
print('Task 2: Generate input data')
input_data = torch.randn(2, 3, 4, 1)
print(input_data)
print('Task 3: Call the API torch.squeeze')
print(torch.squeeze(input_data))
print(torch.squeeze(input_data, dim=2))
print('Task 4: Call the API torch.unsqueeze')
print(torch.unsqueeze(input_data, dim=2))
print(torch.unsqueeze(input_data, dim=3))