'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
_input_tensor = torch.arange(1, 13, dtype=torch.float32).view(3, 4)
print('The input tensor is:\n', _input_tensor)
_output_tensor = _input_tensor.mean(dim=0, keepdim=False)
print('The output tensor is:\n', _output_tensor)