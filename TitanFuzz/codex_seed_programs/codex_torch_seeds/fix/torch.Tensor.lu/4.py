'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lu\ntorch.Tensor.lu(_input_tensor, pivot=True, get_infos=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: \n{}'.format(_input_tensor))
lu_output = torch.Tensor.lu(_input_tensor, pivot=True, get_infos=False)
print('Output of torch.Tensor.lu: \n{}'.format(lu_output))