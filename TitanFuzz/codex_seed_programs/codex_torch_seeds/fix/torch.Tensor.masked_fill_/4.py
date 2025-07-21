'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.arange(1, 11)
print(input_tensor)
mask = torch.tensor([0, 1, 1, 0, 0, 1, 0, 1, 1, 0], dtype=torch.bool)
print(mask)
value = (- 1)
input_tensor.masked_fill_(mask, value)
print(input_tensor)