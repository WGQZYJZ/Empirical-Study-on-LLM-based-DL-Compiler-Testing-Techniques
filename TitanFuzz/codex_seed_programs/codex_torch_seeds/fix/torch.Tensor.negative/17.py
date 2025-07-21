'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input tensor:\n', input_tensor)
output_tensor = torch.Tensor.negative(input_tensor)
print('Output tensor:\n', output_tensor)