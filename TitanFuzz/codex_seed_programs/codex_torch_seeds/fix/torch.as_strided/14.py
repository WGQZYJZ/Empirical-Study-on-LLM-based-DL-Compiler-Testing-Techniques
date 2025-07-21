'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_strided\ntorch.as_strided(input, size, stride, storage_offset=0)\n'
import torch
import torch
input = torch.arange(1, 11)
print(input)
output = torch.as_strided(input, (4, 2), (2, 1))
print(output)
print(output)
input[2] = 100
print(output)
print(output)
output[(0, 0)] = 100
print(output)
print(output)
output[(0, 0)] = 100
print(output)
print(output)
output[(0, 0)] = 100
print(output)