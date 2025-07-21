'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
x = torch.arange(start=0, end=9, step=1)
print(x)
print(torch.Tensor.tensor_split(x, [3, 6], dim=0))