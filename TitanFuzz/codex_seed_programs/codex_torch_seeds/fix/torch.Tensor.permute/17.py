'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.permute(1, 2, 0)
print('Output tensor: \n', output_tensor)