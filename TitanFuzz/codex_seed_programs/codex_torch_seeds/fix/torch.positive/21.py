'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input_data = torch.randn(3, 3)
output_data = torch.positive(input_data)
print('Input data:\n', input_data)
print('Output data:\n', output_data)