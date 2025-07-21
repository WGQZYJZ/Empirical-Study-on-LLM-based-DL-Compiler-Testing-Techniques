'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.rand(1, 3)
output = torch.fmod(input_data, 2)
print(output)