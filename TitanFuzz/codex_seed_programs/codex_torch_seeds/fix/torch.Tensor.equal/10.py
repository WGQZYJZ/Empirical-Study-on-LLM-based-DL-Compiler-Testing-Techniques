'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(5, 5)
other = torch.rand(5, 5)
output_tensor = torch.Tensor.equal(input_tensor, other)
print('Input Tensor: ', input_tensor)
print('Other Tensor: ', other)
print('Output Tensor: ', output_tensor)