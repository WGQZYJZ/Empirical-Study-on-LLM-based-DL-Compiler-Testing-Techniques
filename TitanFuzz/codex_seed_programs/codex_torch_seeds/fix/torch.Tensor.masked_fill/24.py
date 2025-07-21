'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
mask = torch.Tensor([[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]])
value = (- 1)
output_tensor = input_tensor.masked_fill(mask, value)
print(input_tensor)
print(output_tensor)