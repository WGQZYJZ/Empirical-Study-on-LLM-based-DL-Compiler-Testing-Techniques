'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log\ntorch.Tensor.log(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: \n {}'.format(input_tensor))
output_tensor = input_tensor.log()
print('Output tensor: \n {}'.format(output_tensor))