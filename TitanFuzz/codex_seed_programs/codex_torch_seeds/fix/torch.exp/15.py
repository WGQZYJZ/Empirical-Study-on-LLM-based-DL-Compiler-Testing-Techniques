'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.exp\ntorch.exp(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Data: {}'.format(input_data))
output_data = torch.exp(input_data)
print('Output Data: {}'.format(output_data))