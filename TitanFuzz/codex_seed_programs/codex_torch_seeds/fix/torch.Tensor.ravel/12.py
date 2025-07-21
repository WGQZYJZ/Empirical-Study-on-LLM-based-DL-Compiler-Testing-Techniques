'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.rand((4, 4))
print('input_tensor = \n{}'.format(input_tensor))
output_tensor = input_tensor.ravel()
print('output_tensor = \n{}'.format(output_tensor))