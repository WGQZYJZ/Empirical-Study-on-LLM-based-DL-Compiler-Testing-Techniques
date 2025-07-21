'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(2, 3)
value = 2
output_tensor = torch.Tensor.multiply(input_tensor, value)
print('The input tensor is: \n{}'.format(input_tensor))
print('The output tensor is: \n{}'.format(output_tensor))