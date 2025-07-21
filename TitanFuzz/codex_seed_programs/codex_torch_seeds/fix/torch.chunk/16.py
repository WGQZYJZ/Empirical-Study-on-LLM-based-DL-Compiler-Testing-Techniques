'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(input, chunks, dim=0)\n'
import torch
input_data = torch.arange(0, 12)
print(input_data)
output = torch.chunk(input_data, 3, dim=0)
print(output)
print(output[0])
print(output[1])
print(output[2])