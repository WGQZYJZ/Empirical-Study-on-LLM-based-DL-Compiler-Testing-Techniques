'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
output = torch.all(input_data)
print('output = ', output)