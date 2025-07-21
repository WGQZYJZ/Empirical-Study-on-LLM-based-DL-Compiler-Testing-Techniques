'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(input_tensor)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0]])
output_tensor = input_tensor.masked_fill(mask, (- 1))
print('Output tensor:')
print(output_tensor)