'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
input_tensor = torch.arange(0, 12).view(3, 4)
mask = torch.tensor([[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]], dtype=torch.uint8)
'\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
output_tensor = input_tensor.masked_fill(mask, (- 1))
print('input_tensor:', input_tensor)
print('mask:', mask)
print('output_tensor:', output_tensor)