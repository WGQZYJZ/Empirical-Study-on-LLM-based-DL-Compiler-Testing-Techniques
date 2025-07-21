'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('input_data: \n', input_data)
print('input_data.shape: \n', input_data.shape)
chunk_data = torch.chunk(input_data, 2, dim=0)
print('chunk_data: \n', chunk_data)
print('chunk_data[0].shape: \n', chunk_data[0].shape)
print('chunk_data[1].shape: \n', chunk_data[1].shape)
chunk_data = torch.chunk(input_data, 3, dim=0)
print('chunk_data: \n', chunk_data)