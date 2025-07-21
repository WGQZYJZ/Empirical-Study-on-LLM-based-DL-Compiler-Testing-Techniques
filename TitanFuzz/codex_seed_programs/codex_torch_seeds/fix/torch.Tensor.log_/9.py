'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log_\ntorch.Tensor.log_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.log_()
print('Output tensor:')
print(output_tensor)