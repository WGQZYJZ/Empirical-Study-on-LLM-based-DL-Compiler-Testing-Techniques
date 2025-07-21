'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unbind\ntorch.Tensor.unbind(_input_tensor, dim=0)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.unbind(input_tensor, dim=0)
print('output_tensor: ', output_tensor)