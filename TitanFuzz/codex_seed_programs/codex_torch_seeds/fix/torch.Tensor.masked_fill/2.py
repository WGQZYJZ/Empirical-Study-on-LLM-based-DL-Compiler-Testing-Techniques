'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
mask = torch.tensor([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=torch.bool)
value = torch.tensor(100)
print('input_tensor:', input_tensor)
print('mask:', mask)
print('value:', value)
print('input_tensor.shape:', input_tensor.shape)
print('mask.shape:', mask.shape)
print('value.shape:', value.shape)
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)
print('output_tensor:', output_tensor)