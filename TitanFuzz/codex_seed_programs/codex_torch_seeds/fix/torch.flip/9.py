'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flip\ntorch.flip(input, dims)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
print(torch.flip(input_data, [0]))