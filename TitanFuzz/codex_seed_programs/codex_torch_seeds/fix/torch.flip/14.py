'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
print('Input data:\n', input_data)
flipped_data = torch.flip(input_data, dims=[0])
print('Flipped data:\n', flipped_data)