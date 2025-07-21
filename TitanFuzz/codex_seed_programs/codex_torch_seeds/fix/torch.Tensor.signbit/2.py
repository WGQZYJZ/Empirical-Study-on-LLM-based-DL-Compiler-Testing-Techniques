'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(5, 5)
output_tensor = input_tensor.signbit()
print('input_tensor = \n{}'.format(input_tensor))
print('output_tensor = \n{}'.format(output_tensor))