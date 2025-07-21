'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinh\ntorch.Tensor.sinh(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.sinh()
print('output_tensor: ', output_tensor)