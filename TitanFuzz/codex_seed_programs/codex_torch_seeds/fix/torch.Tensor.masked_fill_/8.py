'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(2, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1]])
value = torch.tensor(0.5)
output_tensor = torch.Tensor.masked_fill_(input_tensor, mask, value)
print('input_tensor:')
print(input_tensor)
print('mask:')
print(mask)
print('value:')
print(value)
print('output_tensor:')
print(output_tensor)