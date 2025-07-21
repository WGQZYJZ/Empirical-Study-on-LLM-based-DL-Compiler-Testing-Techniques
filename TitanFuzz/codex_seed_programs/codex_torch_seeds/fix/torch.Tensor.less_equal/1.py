'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_equal\ntorch.Tensor.less_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(4, 4)
output_tensor = input_tensor.less_equal(0.5)
print('Input Tensor:\n', input_tensor)
print('Output Tensor:\n', output_tensor)