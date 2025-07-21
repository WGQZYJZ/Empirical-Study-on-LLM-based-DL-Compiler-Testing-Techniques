'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(4, 4)
mask = torch.tensor([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
value = 0.0
print('input_tensor:', input_tensor)
print('mask:', mask)
print('value:', value)
output_tensor = input_tensor.masked_fill(mask, value)
print('output_tensor:', output_tensor)