'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data:')
print(input_data)
print('Output data:')
print(torch.amin(input_data, dim=1, keepdim=True))