'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 4), dtype=torch.int32)
print('input_tensor = \n{}'.format(input_tensor))
output_tensor = input_tensor.cummin(dim=0)
print('output_tensor = \n{}'.format(output_tensor))