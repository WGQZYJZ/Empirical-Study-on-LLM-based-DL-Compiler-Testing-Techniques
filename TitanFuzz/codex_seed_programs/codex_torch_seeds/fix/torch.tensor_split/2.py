'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
import torch
input = torch.arange(start=1, end=25, dtype=torch.float32).reshape(4, 6)
print(input)
output = torch.tensor_split(input, 3, dim=0)
print(output)
print(len(output))
print(output[0])
print(output[1])
print(output[2])