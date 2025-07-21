'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(input_tensor)
mask = torch.randint(2, size=(3, 3), dtype=torch.bool)
value = torch.randn(1)
print('Mask:')
print(mask)
print('Value:')
print(value)
input_tensor.masked_fill_(mask, value)
print('Output tensor:')
print(input_tensor)