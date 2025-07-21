'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0_\ntorch.Tensor.i0_(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
output_tensor = torch.Tensor.i0_(input_tensor)
print('The input_tensor is:', input_tensor)
print('The output_tensor is:', output_tensor)