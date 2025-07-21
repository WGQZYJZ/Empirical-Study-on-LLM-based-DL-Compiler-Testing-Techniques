'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor: ', input_tensor)
shifts = 1
dims = 1
output_tensor = input_tensor.roll(shifts, dims)
print('output_tensor: ', output_tensor)