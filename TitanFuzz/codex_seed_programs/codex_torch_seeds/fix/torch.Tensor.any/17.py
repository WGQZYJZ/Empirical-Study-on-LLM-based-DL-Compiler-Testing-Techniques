'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input = torch.randn(2, 3)
print('Input:', _input)
_output = torch.Tensor.any(_input)
print('Output:', _output)