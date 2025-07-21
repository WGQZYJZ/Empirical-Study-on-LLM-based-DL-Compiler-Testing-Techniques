'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('input_tensor: ', _input_tensor)
print('output_tensor: ', _output_tensor)