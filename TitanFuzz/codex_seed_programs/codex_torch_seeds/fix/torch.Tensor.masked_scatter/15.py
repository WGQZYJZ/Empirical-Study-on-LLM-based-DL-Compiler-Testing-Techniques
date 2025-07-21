'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
import torch
input_tensor = torch.rand(5, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]])
tensor = torch.rand(5, 3)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)
print('input_tensor: \n', input_tensor)
print('mask: \n', mask)
print('tensor: \n', tensor)
print('output_tensor: \n', output_tensor)