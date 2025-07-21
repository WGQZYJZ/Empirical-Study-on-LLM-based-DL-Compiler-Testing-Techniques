'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
input_tensor = torch.rand(10, 10)
shifts = 1
dims = 0
output_tensor = input_tensor.roll(shifts, dims)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)