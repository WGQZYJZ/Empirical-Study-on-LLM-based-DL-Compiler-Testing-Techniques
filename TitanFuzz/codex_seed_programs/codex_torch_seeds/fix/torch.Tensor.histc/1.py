'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
_input_tensor = torch.rand(1000)
_output_tensor = _input_tensor.histc(bins=100, min=0, max=1)
print(_output_tensor)