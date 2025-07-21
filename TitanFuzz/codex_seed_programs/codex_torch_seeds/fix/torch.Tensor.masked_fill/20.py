'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(5, 5)
mask = torch.ByteTensor([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]])
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, (- 1))
print('Input Tensor:', input_tensor)
print('Mask:', mask)
print('Output Tensor:', output_tensor)