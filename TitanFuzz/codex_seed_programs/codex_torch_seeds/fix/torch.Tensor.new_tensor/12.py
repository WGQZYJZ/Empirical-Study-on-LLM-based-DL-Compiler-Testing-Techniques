'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(10)
output = torch.Tensor.new_tensor(_input_tensor, data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('output: ', output)