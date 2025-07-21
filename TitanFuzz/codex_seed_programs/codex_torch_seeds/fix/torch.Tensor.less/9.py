'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
other = torch.randn(3)
print('other: ', other)
output_tensor = input_tensor.less(other)
print('Output tensor: ', output_tensor)
'\nTask 4: Call the API torch.Tensor.less_equal\ntorch.Tensor.less_equal(_input_tensor, other)\n'
output_tensor = input_tensor.less_equal(other)
print('Output tensor: ', output_tensor)
'\nTask 5: Call the API torch.Tensor.greater\ntorch.Tensor.greater(_input_tensor, other)\n'
output_tensor = input_tensor.greater(other)
print('Output tensor: ', output_tensor)
'\nTask 6: Call the API torch.Tensor.greater_equal\ntorch.Tensor.greater_equal(_input_tensor, other)\n'