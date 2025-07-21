'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input = torch.randn(20, 16)
(chunk1, chunk2) = torch.tensor_split(input, 2, dim=1)
print(chunk1.shape)
print(chunk2.shape)