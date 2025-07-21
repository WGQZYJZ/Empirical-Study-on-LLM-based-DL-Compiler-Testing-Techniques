'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
data = torch.arange(16)
print(data)
out = torch.tensor_split(data, 4, dim=0)
print(out)
out = torch.tensor_split(data, 4, dim=0)
for i in out:
    print(i)
out = torch.tensor_split(data, [4, 6, 10], dim=0)
for i in out:
    print(i)