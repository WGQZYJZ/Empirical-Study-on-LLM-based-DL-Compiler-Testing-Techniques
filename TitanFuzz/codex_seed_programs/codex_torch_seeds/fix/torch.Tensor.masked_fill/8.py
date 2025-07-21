'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(4, 4)
mask = torch.tensor([[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]], dtype=torch.bool)
value = torch.tensor(1.0)
print('Input Tensor:')
print(input_tensor)
print('Mask:')
print(mask)
output_tensor = input_tensor.masked_fill(mask, value)
print('Output Tensor:')
print(output_tensor)