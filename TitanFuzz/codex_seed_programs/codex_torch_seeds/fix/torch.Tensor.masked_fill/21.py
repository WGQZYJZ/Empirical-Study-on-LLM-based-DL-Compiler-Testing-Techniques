'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor = ', input_tensor)
mask = torch.tensor([[0, 1, 0], [1, 1, 0]], dtype=torch.uint8)
value = torch.tensor(1.0)
output_tensor = input_tensor.masked_fill(mask, value)
print('output_tensor = ', output_tensor)