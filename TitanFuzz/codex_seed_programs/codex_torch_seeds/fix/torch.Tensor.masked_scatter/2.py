'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
import torch
input_tensor = torch.rand((3, 3))
print('input_tensor: ', input_tensor)
mask = torch.tensor([[0, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=torch.uint8)
print('mask: ', mask)
tensor = torch.rand((3, 3))
print('tensor: ', tensor)
output_tensor = input_tensor.masked_scatter(mask, tensor)
print('output_tensor: ', output_tensor)