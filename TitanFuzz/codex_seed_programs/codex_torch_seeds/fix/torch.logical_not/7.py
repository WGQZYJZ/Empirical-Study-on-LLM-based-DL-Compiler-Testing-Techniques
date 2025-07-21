'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
input_data = torch.tensor([[0, 1, 0], [1, 0, 1]], dtype=torch.bool)
print('\nInput data:\n', input_data)
output_data = torch.logical_not(input_data)
print('\nOutput data:\n', output_data)