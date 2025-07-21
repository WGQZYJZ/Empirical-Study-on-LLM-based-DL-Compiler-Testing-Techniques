'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
output_data = torch.chunk(input_data, 2, dim=0)
print(output_data)