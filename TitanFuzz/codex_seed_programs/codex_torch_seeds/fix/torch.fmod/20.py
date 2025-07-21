'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
output_data = torch.fmod(input_data, 2)
print(output_data)