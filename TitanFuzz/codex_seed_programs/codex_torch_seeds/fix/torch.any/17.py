'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
print('Input Data: \n', input_data)
output_data = torch.any(input_data, dim=1)
print('Output Data: \n', output_data)