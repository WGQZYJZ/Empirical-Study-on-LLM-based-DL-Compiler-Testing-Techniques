'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unfold\ntorch.Tensor.unfold(_input_tensor, dimension, size, step)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.arange(0, 24).view(2, 3, 4)
print('input_tensor = \n{}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.unfold')
output_tensor = input_tensor.unfold(dimension=0, size=1, step=1)
print('output_tensor = \n{}'.format(output_tensor))