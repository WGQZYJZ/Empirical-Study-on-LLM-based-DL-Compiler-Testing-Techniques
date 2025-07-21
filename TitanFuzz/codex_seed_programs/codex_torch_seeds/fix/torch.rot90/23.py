'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input_data = torch.rand(2, 3, 4)
print(input_data)
print(torch.rot90(input_data, 1, (0, 2)))
print(torch.rot90(input_data, 2, (0, 2)))