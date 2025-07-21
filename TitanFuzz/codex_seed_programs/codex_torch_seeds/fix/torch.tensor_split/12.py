'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
import torch
input = torch.randn(20, 6)
print(f'input size: {input.size()}')
indices_or_sections = [3, 5, 6, 5]
output = torch.tensor_split(input, indices_or_sections, dim=0)
print(f'output size: {len(output)}')
for tensor in output:
    print(f'tensor size: {tensor.size()}')
indices_or_sections = 4
output = torch.tensor_split(input, indices_or_sections, dim=0)
print(f'output size: {len(output)}')
for tensor in output:
    print(f'tensor size: {tensor.size()}')