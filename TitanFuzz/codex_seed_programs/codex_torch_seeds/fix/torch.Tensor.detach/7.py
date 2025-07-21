'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(1, 3, 3, 3)
_output_tensor = _input_tensor.detach()
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)