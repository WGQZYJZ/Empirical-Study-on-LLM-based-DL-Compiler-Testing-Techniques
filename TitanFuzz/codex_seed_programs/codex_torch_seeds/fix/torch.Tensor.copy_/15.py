'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor = \n{}'.format(input_tensor))
src = torch.rand(3, 2)
print('src = \n{}'.format(src))
output_tensor = input_tensor.copy_(src)
print('output_tensor = \n{}'.format(output_tensor))