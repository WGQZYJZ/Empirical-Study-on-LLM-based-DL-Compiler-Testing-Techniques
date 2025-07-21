'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4))
mask = torch.Tensor([[1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]).bool()
value = 10
output_tensor = input_tensor.masked_fill(mask, value)
print('input tensor:')
print(input_tensor)
print('mask:')
print(mask)
print('value:')
print(value)
print('output tensor:')
print(output_tensor)