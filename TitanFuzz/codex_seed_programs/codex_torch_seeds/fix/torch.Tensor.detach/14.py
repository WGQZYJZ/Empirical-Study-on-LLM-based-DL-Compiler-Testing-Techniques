'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
import torch
_input_tensor = torch.rand(2, 3, requires_grad=True)
_output_tensor = torch.Tensor.detach(_input_tensor)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)