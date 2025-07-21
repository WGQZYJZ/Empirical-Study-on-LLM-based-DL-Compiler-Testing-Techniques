'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.angle(input_tensor)
print('input_tensor = \n', input_tensor)
print('output_tensor = \n', output_tensor)