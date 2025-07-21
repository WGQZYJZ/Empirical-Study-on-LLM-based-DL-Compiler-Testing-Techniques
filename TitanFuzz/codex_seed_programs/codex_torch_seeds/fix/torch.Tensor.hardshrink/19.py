'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data is: \n{}'.format(input_data))
shrinked_data = torch.Tensor.hardshrink(input_data, lambd=0.5)
print('Shrinked data is: \n{}'.format(shrinked_data))