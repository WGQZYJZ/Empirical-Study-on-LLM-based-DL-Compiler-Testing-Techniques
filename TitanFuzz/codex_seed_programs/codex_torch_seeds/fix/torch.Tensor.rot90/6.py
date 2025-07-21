'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: ', input_tensor)
rotate_tensor = torch.Tensor.rot90(input_tensor, 2, [0, 1])
print('Rotated tensor: ', rotate_tensor)