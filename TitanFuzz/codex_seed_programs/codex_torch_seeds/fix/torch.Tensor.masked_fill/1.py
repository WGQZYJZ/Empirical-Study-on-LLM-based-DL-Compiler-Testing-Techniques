'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
mask = (input_tensor < 0)
print(mask)
input_tensor.masked_fill(mask, 0)
print(input_tensor)