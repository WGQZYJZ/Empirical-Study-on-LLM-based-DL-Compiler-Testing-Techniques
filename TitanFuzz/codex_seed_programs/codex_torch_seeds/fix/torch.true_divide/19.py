'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.true_divide\ntorch.true_divide(dividend, divisor, *, out)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
divisor = torch.randn(3)
divisor = divisor.view(1, 3)
print('Divisor: ', divisor)
output_tensor = torch.true_divide(input_tensor, divisor)
print('Output Tensor: ', output_tensor)
print('Output Tensor Size: ', output_tensor.size())