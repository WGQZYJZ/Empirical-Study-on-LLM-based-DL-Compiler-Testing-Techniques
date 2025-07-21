'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
_input_tensor = input_tensor.clone()
dims = [4, 1]
output_tensor = _input_tensor.tile(dims)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)