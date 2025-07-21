'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float32)
print('Input Tensor: \n{}'.format(input_tensor))
output_tensor = torch.Tensor.floor_divide_(input_tensor, 5)
print('Output Tensor: \n{}'.format(output_tensor))