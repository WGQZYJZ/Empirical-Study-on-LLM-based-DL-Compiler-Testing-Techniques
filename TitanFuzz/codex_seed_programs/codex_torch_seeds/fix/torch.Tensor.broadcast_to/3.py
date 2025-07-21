'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (3, 4, 5, 3))
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)