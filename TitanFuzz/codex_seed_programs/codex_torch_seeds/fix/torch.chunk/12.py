'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print('input_data.shape:', input_data.shape)
output = torch.chunk(input_data, 3, dim=1)
print('output:', output)
print('output[0].shape:', output[0].shape)
print('output[1].shape:', output[1].shape)
print('output[2].shape:', output[2].shape)