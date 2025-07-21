'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('Input data:\n', input_data)
flipped_data = torch.flipud(input_data)
print('Flipped data:\n', flipped_data)