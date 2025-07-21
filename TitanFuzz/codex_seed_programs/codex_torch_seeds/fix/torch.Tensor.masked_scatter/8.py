'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
mask = torch.tensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]], dtype=torch.uint8)
print('Input tensor: \n', input_tensor)
print('Mask: \n', mask)
output_tensor = input_tensor.masked_scatter(mask, torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print('Output tensor: \n', output_tensor)