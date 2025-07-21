'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_strided\ntorch.as_strided(input, size, stride, storage_offset=0)\n'
import torch
input = torch.arange(0, 20)
print(input)
output = torch.as_strided(input, (3, 4), (4, 1))
print(output)